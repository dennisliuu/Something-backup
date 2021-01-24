<?php

namespace App\Http\Controllers;

use App\Http\Requests\CreateassetRequest;
use App\Http\Requests\UpdateassetRequest;
use App\Repositories\assetRepository;
use App\Http\Controllers\AppBaseController;
use Illuminate\Http\Request;
use Flash;
use Response;

class assetController extends AppBaseController
{
    /** @var  assetRepository */
    private $assetRepository;

    public function __construct(assetRepository $assetRepo)
    {
        $this->assetRepository = $assetRepo;
    }

    /**
     * Display a listing of the asset.
     *
     * @param Request $request
     *
     * @return Response
     */
    public function index(Request $request)
    {
        $assets = $this->assetRepository->all();

        return view('assets.index')
            ->with('assets', $assets);
    }

    /**
     * Show the form for creating a new asset.
     *
     * @return Response
     */
    public function create()
    {
        return view('assets.create');
    }

    /**
     * Store a newly created asset in storage.
     *
     * @param CreateassetRequest $request
     *
     * @return Response
     */
    public function store(CreateassetRequest $request)
    {
        $image = $request->file('image');
        \Storage::disk('public')->put($image->getClientOriginalName(), $image);
        $input = $request->all();
        $input["image"] = env('APP_URL').'/img/' .$image->getClientOriginalName().'/'. $image->hashName();
        $asset = $this->assetRepository->create($input);

        Flash::success('Asset saved successfully.');

        return redirect(route('assets.index'));
    }

    /**
     * Display the specified asset.
     *
     * @param int $id
     *
     * @return Response
     */
    public function show($id)
    {
        $asset = $this->assetRepository->find($id);

        if (empty($asset)) {
            Flash::error('Asset not found');

            return redirect(route('assets.index'));
        }

        return view('assets.show')->with('asset', $asset);
    }

    /**
     * Show the form for editing the specified asset.
     *
     * @param int $id
     *
     * @return Response
     */
    public function edit($id)
    {
        $asset = $this->assetRepository->find($id);

        if (empty($asset)) {
            Flash::error('Asset not found');

            return redirect(route('assets.index'));
        }

        return view('assets.edit')->with('asset', $asset);
    }

    /**
     * Update the specified asset in storage.
     *
     * @param int $id
     * @param UpdateassetRequest $request
     *
     * @return Response
     */
    public function update($id, UpdateassetRequest $request)
    {
        $asset = $this->assetRepository->find($id);

        if (empty($asset)) {
            Flash::error('Asset not found');

            return redirect(route('assets.index'));
        }

        $asset = $this->assetRepository->update($request->all(), $id);

        Flash::success('Asset updated successfully.');

        return redirect(route('assets.index'));
    }

    /**
     * Remove the specified asset from storage.
     *
     * @param int $id
     *
     * @throws \Exception
     *
     * @return Response
     */
    public function destroy($id)
    {
        $asset = $this->assetRepository->find($id);

        if (empty($asset)) {
            Flash::error('Asset not found');

            return redirect(route('assets.index'));
        }

        $this->assetRepository->delete($id);

        Flash::success('Asset deleted successfully.');

        return redirect(route('assets.index'));
    }
}
