# 🚀 Streamlit Cloud 배포 완벽 가이드

## 📋 배포 전 체크리스트

- [ ] GitHub 계정 보유
- [ ] 저장소에 다음 파일 업로드 완료:
  - [ ] `app.py`
  - [ ] `requirements.txt`
  - [ ] `README.md`
- [ ] 로컬에서 정상 작동 확인

## 🎯 단계별 배포 가이드

### 1️⃣ GitHub 저장소 생성

1. GitHub 접속 → **"New repository"** 클릭
2. 저장소 이름 입력 (예: `ai-background-remover`)
3. **Public** 선택 (중요: Streamlit Cloud는 Public 저장소만 무료)
4. **"Create repository"** 클릭

### 2️⃣ 파일 업로드

**방법 A: GitHub 웹에서 직접 업로드**
```
1. 생성된 저장소 페이지에서 "uploading an existing file" 클릭
2. app.py, requirements.txt, README.md 드래그 앤 드롭
3. "Commit changes" 클릭
```

**방법 B: Git 명령어 사용**
```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/your-username/your-repo.git
git branch -M main
git push -u origin main
```

### 3️⃣ Streamlit Cloud 배포

1. **[share.streamlit.io](https://share.streamlit.io)** 접속
2. **"Sign in with GitHub"** 클릭
3. GitHub 계정으로 로그인 및 권한 승인
4. 메인 대시보드에서 **"New app"** 클릭
5. 배포 설정:
   - **Repository**: 방금 생성한 저장소 선택
   - **Branch**: `main`
   - **Main file path**: `app.py`
6. **"Deploy!"** 클릭

### 4️⃣ 배포 완료 대기

- 배포 진행 상태가 실시간으로 표시됩니다
- 약 2~5분 소요 (첫 배포는 조금 더 걸릴 수 있음)
- 로그에서 "Your app is live!" 메시지 확인

### 5️⃣ 앱 URL 확인

배포 완료 시 자동으로 생성되는 URL 형식:
```
https://your-app-name-random-string.streamlit.app
```

## 🔧 배포 후 관리

### 앱 업데이트 방법
GitHub 저장소의 코드를 수정하면 **자동으로 재배포**됩니다!

```bash
# 코드 수정 후
git add .
git commit -m "Update: 기능 개선"
git push
```

### 앱 설정 변경
Streamlit Cloud 대시보드에서:
- ⚙️ Settings → 앱 이름, Python 버전 변경 가능
- 🔄 Reboot app → 앱 재시작
- 🗑️ Delete app → 앱 삭제

### 로그 확인
- 📋 **Logs** 탭에서 실시간 로그 확인 가능
- 오류 발생 시 여기서 디버깅

## ⚡ 최적화 팁

### 1. 첫 로딩 속도 개선
`app.py` 상단에 캐싱 추가:

```python
@st.cache_resource
def load_model():
    # 모델 로딩 로직
    pass
```

### 2. 메모리 관리
대용량 이미지 처리 시:
```python
# 이미지 리사이징
max_size = 2000
if image.size[0] > max_size or image.size[1] > max_size:
    image.thumbnail((max_size, max_size))
```

### 3. 사용자 경험 개선
```python
# 진행 상태 표시
with st.spinner('처리 중...'):
    result = remove_background(image)
```

## 🐛 문제 해결

### "ModuleNotFoundError"
→ `requirements.txt`에 해당 라이브러리 추가

### "App is sleeping"
→ 무료 플랜은 일정 시간 미사용 시 sleep 모드
→ 앱 방문 시 자동으로 다시 활성화

### 메모리 초과 오류
→ 이미지 크기 제한 또는 리사이징 로직 추가

## 💰 비용

Streamlit Community Cloud는 **완전 무료**입니다!
- 제한: Public 저장소만 가능
- 리소스: 1GB RAM, 1 CPU core
- 앱 개수: 계정당 최대 3개

더 많은 리소스가 필요하면 Streamlit Cloud Teams 플랜 고려

## 📚 추가 자료

- [Streamlit 공식 문서](https://docs.streamlit.io)
- [Streamlit Cloud 문서](https://docs.streamlit.io/streamlit-community-cloud)
- [rembg GitHub](https://github.com/danielgatis/rembg)

---

**이제 여러분의 AI 앱을 전 세계와 공유하세요! 🌍✨**
