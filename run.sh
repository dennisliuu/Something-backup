#!/bin/sh
echo "Running with ${1}"

# a = ${1##*.}
# echo $(a)

# echo ${1%%"."*} before
# echo ${1#*"."} after

case ${1##*.} in
	"c")
		clang ${1} -o ${1%%"."*}.out && ./${1%%"."*}.out
		;;
	"cpp")
		clang++ ${1} -o ${1%%"."*}.out && ./${1%%"."*}.out
		;;
	"python")
		pytho3 ${1}
		;;
	*)
		echo "${1##*.} is unknow file types"
		;;
esac
#etc.
