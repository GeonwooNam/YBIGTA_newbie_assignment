
# anaconda(또는 miniconda)가 존재하지 않을 경우 설치해주세요!
## TODO
# conda가 없으면 miniconda 설치
if ! command -v conda >/dev/null 2>&1; then
    echo "[INFO] conda not found. Installing Miniconda..."

    MINICONDA_DIR="$HOME/miniconda3"
    INSTALLER="Miniconda3-latest-Linux-x86_64.sh"

    wget -q https://repo.anaconda.com/miniconda/$INSTALLER -O /tmp/$INSTALLER
    bash /tmp/$INSTALLER -b -p "$MINICONDA_DIR"

    # 현재 쉘에서 conda 사용 가능하게 설정
    source "$MINICONDA_DIR/etc/profile.d/conda.sh"
else
    # 이미 conda가 있더라도 현재 쉘에 연결
    source "$(conda info --base)/etc/profile.d/conda.sh"
fi

# Conda 환셩 생성 및 활성화
## TODO
echo "[INFO] Conda 환경 생성 및 활성화"
conda create --name myenv python=3.11 -y
conda activate myenv

## 건드리지 마세요! ##
python_env=$(python -c "import sys; print(sys.prefix)")
if [[ "$python_env" == *"/envs/myenv"* ]]; then
    echo "[INFO] 가상환경 활성화: 성공"
else
    echo "[INFO] 가상환경 활성화: 실패"
    exit 1 
fi

# 필요한 패키지 설치
## TODO
echo "[INFO] mypy 설치"
conda install -y mypy

# Submission 폴더 파일 실행
cd submission || { echo "[INFO] submission 디렉토리로 이동 실패"; exit 1; }

for file in *.py; do
    ## TODO
    # 파일명에서 문제 번호 추출 (예: 1_1260.py -> 1260)
    problem_num=$(basename "$file" .py | cut -d'_' -f2)

    input_file="../input/${problem_num}_input"
    output_file="../output/${problem_num}_output"

    echo "[INFO] Running $file with input $input_file"

    python "$file" < "$input_file" > "$output_file"

done

# mypy 테스트 실행 및 mypy_log.txt 저장
## TODO
echo "[INFO] mypy 테스트 실행"
mypy *.py > ../mypy_log.txt

# conda.yml 파일 생성
## TODO
echo "[INFO] conda.yml 파일 생성"
conda env export > ../conda.yml

# 가상환경 비활성화
## TODO
conda deactivate
