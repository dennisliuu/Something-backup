<?php namespace Tests\Repositories;

use App\Models\products;
use App\Repositories\productsRepository;
use Illuminate\Foundation\Testing\DatabaseTransactions;
use Tests\TestCase;
use Tests\ApiTestTrait;

class productsRepositoryTest extends TestCase
{
    use ApiTestTrait, DatabaseTransactions;

    /**
     * @var productsRepository
     */
    protected $productsRepo;

    public function setUp() : void
    {
        parent::setUp();
        $this->productsRepo = \App::make(productsRepository::class);
    }

    /**
     * @test create
     */
    public function test_create_products()
    {
        $products = factory(products::class)->make()->toArray();

        $createdproducts = $this->productsRepo->create($products);

        $createdproducts = $createdproducts->toArray();
        $this->assertArrayHasKey('id', $createdproducts);
        $this->assertNotNull($createdproducts['id'], 'Created products must have id specified');
        $this->assertNotNull(products::find($createdproducts['id']), 'products with given id must be in DB');
        $this->assertModelData($products, $createdproducts);
    }

    /**
     * @test read
     */
    public function test_read_products()
    {
        $products = factory(products::class)->create();

        $dbproducts = $this->productsRepo->find($products->id);

        $dbproducts = $dbproducts->toArray();
        $this->assertModelData($products->toArray(), $dbproducts);
    }

    /**
     * @test update
     */
    public function test_update_products()
    {
        $products = factory(products::class)->create();
        $fakeproducts = factory(products::class)->make()->toArray();

        $updatedproducts = $this->productsRepo->update($fakeproducts, $products->id);

        $this->assertModelData($fakeproducts, $updatedproducts->toArray());
        $dbproducts = $this->productsRepo->find($products->id);
        $this->assertModelData($fakeproducts, $dbproducts->toArray());
    }

    /**
     * @test delete
     */
    public function test_delete_products()
    {
        $products = factory(products::class)->create();

        $resp = $this->productsRepo->delete($products->id);

        $this->assertTrue($resp);
        $this->assertNull(products::find($products->id), 'products should not exist in DB');
    }
}
