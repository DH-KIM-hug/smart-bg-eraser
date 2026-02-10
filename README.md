# ✨ AI 배경 제거기

AI를 활용한 자동 이미지 배경 제거 웹 애플리케이션입니다.

## 🎯 주요 기능

- **간편한 업로드**: Drag & Drop 방식으로 이미지 업로드
- **AI 자동 처리**: U²-Net 기반 딥러닝 모델로 정확한 배경 분리
- **실시간 비교**: Before & After 이미지를 나란히 비교
- **투명 PNG 다운로드**: 투명 배경이 적용된 PNG 파일 즉시 다운로드

## 🚀 로컬 실행 방법

### 1. 저장소 클론
```bash
git clone <your-repo-url>
cd <your-repo-name>
```

### 2. 가상환경 생성 및 활성화
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. 필요 라이브러리 설치
```bash
pip install -r requirements.txt
```

### 4. 애플리케이션 실행
```bash
streamlit run app.py
```

브라우저에서 자동으로 `http://localhost:8501`이 열립니다!

## 📦 배포 방법 (Streamlit Community Cloud)

### 1단계: GitHub 저장소 준비
1. GitHub에 새 저장소 생성
2. 다음 파일들을 저장소에 업로드:
   - `app.py` (메인 애플리케이션)
   - `requirements.txt` (필요 라이브러리)
   - `README.md` (이 파일)

### 2단계: Streamlit Cloud 배포
1. [share.streamlit.io](https://share.streamlit.io) 접속
2. GitHub 계정으로 로그인
3. **"New app"** 클릭
4. 저장소, 브랜치, 파일(`app.py`) 선택
5. **"Deploy!"** 클릭

### 3단계: 완료!
몇 분 후 공개 URL이 생성됩니다. 전 세계 누구나 접속 가능한 무료 웹 서비스 완성! 🎉

## 💡 사용 팁

- **첫 실행**: AI 모델(약 170MB) 다운로드로 30초~1분 소요
- **최적 이미지**: 인물, 제품, 반려동물 사진에서 뛰어난 성능
- **파일 형식**: PNG, JPG, JPEG 지원
- **결과물**: 투명 배경 PNG 파일

## 🛠️ 기술 스택

- **Frontend**: Streamlit
- **AI Engine**: rembg (U²-Net 모델)
- **Image Processing**: Pillow, NumPy
- **Deployment**: Streamlit Community Cloud

## ⚠️ 주의사항

- 대용량 이미지(10MB 이상)는 처리 시간이 길어질 수 있습니다
- 무료 호스팅의 경우 메모리 제한이 있을 수 있습니다
- 상업적 사용 시 rembg 라이브러리의 라이선스를 확인하세요

## 📝 라이선스

이 프로젝트는 오픈소스이며, 자유롭게 사용 및 수정 가능합니다.

## 🤝 기여

버그 리포트, 기능 제안, Pull Request 환영합니다!

---

**Made with ❤️ using Streamlit & rembg**
