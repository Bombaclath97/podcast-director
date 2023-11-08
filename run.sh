#!/usr/bin/bash

pushd "$(dirname "${0}")" || exit

python src/diarization.py
python src/video_creator.py

rm -rf tmp/

popd || exit