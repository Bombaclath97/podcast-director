# podcast-director

Simple podcast director. How to use:

0. Install requirements using pip (`pip install -r requirements.txt`)
1. Create an `input` folder
2. In the `input` folder add the three video sources:
   1. wide_angle.mp4: The camera that records to the whole scene
   2. host_angle.mp4: The camera pointed to the host
   3. guest_angle.mp4: The camera pointed to the guest
3. Get a token on HuggingFace and request access to the following models: [segmentation-3.0](https://huggingface.co/pyannote/segmentation-3.0), [speaker-diarization-3.0](https://huggingface.co/pyannote/speaker-diarization-3.0) 
4. Create a `.env` file and add the token. Follow the `env.example` structure
5. Run the `run` script that's best suited for your OS (Windows: `run.ps1`, UNIX: `run.sh`)

On a successful run, you will find in the `output` folder an `output.mp4` file with a decent guess on what to record in the scene