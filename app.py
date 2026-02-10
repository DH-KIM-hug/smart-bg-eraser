import streamlit as st
from rembg import remove
from PIL import Image
import io
import base64

# 페이지 설정
st.set_page_config(
    page_title="✨ AI 배경 제거기",
    page_icon="🎨",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 커스텀 CSS
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stButton>button {
        width: 100%;
        background-color: #FF4B4B;
        color: white;
        border-radius: 10px;
        padding: 0.5rem 1rem;
        font-weight: bold;
        border: none;
        transition: all 0.3s;
    }
    .stButton>button:hover {
        background-color: #FF6B6B;
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(255, 75, 75, 0.3);
    }
    .upload-text {
        text-align: center;
        color: #666;
        font-size: 1.1rem;
        margin: 1rem 0;
    }
    </style>
""", unsafe_allow_html=True)

def remove_background(image):
    """배경 제거 함수"""
    try:
        # rembg를 사용하여 배경 제거
        output = remove(image)
        return output
    except Exception as e:
        st.error(f"배경 제거 중 오류가 발생했습니다: {str(e)}")
        return None

def get_image_download_link(img, filename="background_removed.png"):
    """다운로드 링크 생성"""
    buffered = io.BytesIO()
    img.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode()
    return img_str

# 메인 타이틀
st.markdown("<h1 style='text-align: center; color: #FF4B4B;'>✨ AI 배경 제거기</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #666; font-size: 1.2rem;'>이미지를 업로드하면 AI가 자동으로 배경을 제거해드립니다</p>", unsafe_allow_html=True)

st.markdown("---")

# 파일 업로더
uploaded_file = st.file_uploader(
    "이미지를 선택하거나 드래그 앤 드롭하세요",
    type=["png", "jpg", "jpeg"],
    help="PNG, JPG, JPEG 형식의 이미지 파일을 업로드할 수 있습니다"
)

if uploaded_file is not None:
    # 원본 이미지 로드
    input_image = Image.open(uploaded_file)
    
    # 진행 상황 표시
    with st.spinner('🎨 AI가 배경을 분석하고 제거하는 중입니다... 잠시만 기다려주세요!'):
        # 배경 제거 실행
        output_image = remove_background(input_image)
    
    if output_image is not None:
        st.success('✅ 배경 제거가 완료되었습니다!')
        
        # Before & After 비교
        st.markdown("### 📊 결과 비교")
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("<p style='text-align: center; font-weight: bold; color: #666;'>원본 이미지</p>", unsafe_allow_html=True)
            st.image(input_image, use_container_width=True)
            st.markdown(f"<p style='text-align: center; color: #999; font-size: 0.9rem;'>크기: {input_image.size[0]} x {input_image.size[1]} px</p>", unsafe_allow_html=True)
        
        with col2:
            st.markdown("<p style='text-align: center; font-weight: bold; color: #FF4B4B;'>배경 제거됨 ✨</p>", unsafe_allow_html=True)
            st.image(output_image, use_container_width=True)
            st.markdown(f"<p style='text-align: center; color: #999; font-size: 0.9rem;'>크기: {output_image.size[0]} x {output_image.size[1]} px</p>", unsafe_allow_html=True)
        
        st.markdown("---")
        
        # 다운로드 버튼
        st.markdown("### 💾 결과 다운로드")
        
        # 이미지를 바이트로 변환
        buf = io.BytesIO()
        output_image.save(buf, format='PNG')
        byte_im = buf.getvalue()
        
        col_download = st.columns([1, 2, 1])
        with col_download[1]:
            st.download_button(
                label="📥 투명 배경 PNG 다운로드",
                data=byte_im,
                file_name="background_removed.png",
                mime="image/png",
                use_container_width=True
            )
        
        # 추가 정보
        st.markdown("---")
        st.markdown("""
        <div style='background-color: #f0f2f6; padding: 1.5rem; border-radius: 10px; margin-top: 2rem;'>
            <h4 style='color: #FF4B4B; margin-top: 0;'>💡 사용 팁</h4>
            <ul style='color: #666;'>
                <li>인물 사진, 제품 사진에 최적화되어 있습니다</li>
                <li>복잡한 배경도 AI가 자동으로 인식합니다</li>
                <li>다운로드한 PNG 파일은 투명 배경으로 어디든 사용 가능합니다</li>
                <li>처리 시간은 이미지 크기에 따라 5~30초 소요됩니다</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

else:
    # 업로드 전 안내 메시지
    st.markdown("""
    <div style='text-align: center; padding: 3rem; background-color: #f8f9fa; border-radius: 15px; margin: 2rem 0;'>
        <h3 style='color: #FF4B4B;'>🎯 이렇게 사용하세요</h3>
        <ol style='text-align: left; display: inline-block; color: #666; font-size: 1.1rem; line-height: 2;'>
            <li>위의 업로드 영역을 클릭하거나 이미지를 드래그 앤 드롭</li>
            <li>AI가 자동으로 배경을 분석하고 제거</li>
            <li>원본과 결과를 비교하고 투명 PNG 다운로드</li>
        </ol>
    </div>
    """, unsafe_allow_html=True)
    
    # 예시 이미지 섹션
    st.markdown("### 📸 활용 예시")
    col_example = st.columns(3)
    
    with col_example[0]:
        st.markdown("""
        <div style='background-color: #fff; padding: 1rem; border-radius: 10px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);'>
            <h4 style='color: #FF4B4B;'>👤 인물 사진</h4>
            <p style='color: #666;'>증명사진, 프로필 사진 배경 제거</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col_example[1]:
        st.markdown("""
        <div style='background-color: #fff; padding: 1rem; border-radius: 10px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);'>
            <h4 style='color: #FF4B4B;'>🛍️ 제품 사진</h4>
            <p style='color: #666;'>온라인 쇼핑몰 상품 이미지</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col_example[2]:
        st.markdown("""
        <div style='background-color: #fff; padding: 1rem; border-radius: 10px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);'>
            <h4 style='color: #FF4B4B;'>🐾 반려동물</h4>
            <p style='color: #666;'>귀여운 반려동물 사진 편집</p>
        </div>
        """, unsafe_allow_html=True)

# 푸터
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #999; padding: 2rem;'>
    <p>Powered by <strong>rembg</strong> (U²-Net AI Model) & <strong>Streamlit</strong></p>
    <p style='font-size: 0.9rem;'>⚡ 첫 실행 시 AI 모델 다운로드로 약 30초 소요될 수 있습니다</p>
</div>
""", unsafe_allow_html=True)
