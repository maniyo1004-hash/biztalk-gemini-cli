const API_BASE = "http://localhost:8000";

document.addEventListener("DOMContentLoaded", () => {
    const targetButtons = document.querySelectorAll(".target-btn");
    const convertBtn = document.getElementById("convertBtn");
    const copyBtn = document.getElementById("copyBtn");
    const inputText = document.getElementById("inputText");
    const outputText = document.getElementById("outputText");
    const loader = document.getElementById("loader");

    let selectedTarget = null;

    // 1. 수신 대상 버튼 토글 로직
    targetButtons.forEach(button => {
        button.addEventListener("click", () => {
            // 기존 활성화 제거
            targetButtons.forEach(btn => btn.classList.remove("active"));
            
            // 현재 버튼 활성화
            button.classList.add("active");
            selectedTarget = button.dataset.target;
        });
    });

    // 2. 변환하기 버튼 클릭 이벤트
    convertBtn.addEventListener("click", async () => {
        const text = inputText.value.trim();

        if (!text) {
            alert("원문을 입력해주세요.");
            inputText.focus();
            return;
        }

        if (!selectedTarget) {
            alert("수신 대상을 선택해주세요.");
            return;
        }

        // 로딩 상태 시작
        setLoading(true);

        try {
            const response = await fetch(`${API_BASE}/api/convert`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({
                    text: text,
                    target_audience: selectedTarget
                }),
            });

            if (!response.ok) {
                const errorData = await response.json();
                throw new Error(errorData.detail || "변환 중 오류가 발생했습니다.");
            }

            const data = await response.json();
            outputText.value = data.converted_text;
            
        } catch (error) {
            console.error("Error:", error);
            alert(`오류 발생: ${error.message}`);
        } finally {
            // 로딩 상태 종료
            setLoading(false);
        }
    });

    // 3. 복사하기 버튼 클릭 이벤트
    copyBtn.addEventListener("click", () => {
        const text = outputText.value;
        if (!text) {
            alert("복사할 내용이 없습니다.");
            return;
        }

        navigator.clipboard.writeText(text).then(() => {
            const originalText = copyBtn.innerText;
            copyBtn.innerText = "복사 완료!";
            copyBtn.classList.add("success");
            
            setTimeout(() => {
                copyBtn.innerText = originalText;
                copyBtn.classList.remove("success");
            }, 2000);
        }).catch(err => {
            console.error("Copy failed:", err);
            alert("클립보드 복사에 실패했습니다.");
        });
    });

    // 로딩 상태 제어 함수
    function setLoading(isLoading) {
        if (isLoading) {
            loader.classList.remove("hidden");
            convertBtn.disabled = true;
            convertBtn.innerText = "변환 중...";
        } else {
            loader.classList.add("hidden");
            convertBtn.disabled = false;
            convertBtn.innerText = "변환하기";
        }
    }
});
