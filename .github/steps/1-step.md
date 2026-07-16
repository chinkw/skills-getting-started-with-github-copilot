## Step 1: Copilot과 첫 만남

**"GitHub Copilot 시작하기"** 실습에 오신 것을 환영합니다! :robot:

이 실습에서는 다양한 GitHub Copilot 기능을 사용하여 Mergington 고등학교 학생들이 과외 활동에 등록할 수 있는 웹사이트를 작업합니다. 🎻 ⚽️ ♟️

<img width="600" alt="Mergington 고등학교 웹앱 스크린샷" src="https://raw.githubusercontent.com/skills-kr/getting-started-with-github-copilot/main/.github/images/mergington-high-school-webapp.png" />

### 📖 이론: GitHub Copilot 알아보기

<img width="150" align="right" alt="copilot 로고" src="https://raw.githubusercontent.com/skills-kr/getting-started-with-github-copilot/main/.github/images/copilot-logo.png" />

GitHub Copilot은 더 빠르고 적은 노력으로 코드를 작성할 수 있도록 도와주는 AI 코딩 어시스턴트로, 문제 해결과 협업에 더 많은 에너지를 집중할 수 있게 해줍니다.

GitHub Copilot은 개발자 생산성을 높이고 소프트웨어 개발 속도를 가속화하는 것으로 입증되었습니다. 자세한 내용은 [GitHub 블로그의 연구: GitHub Copilot이 개발자 생산성과 만족도에 미치는 영향 정량화](https://github.blog/news-insights/research/research-quantifying-github-copilots-impact-on-developer-productivity-and-happiness/)를 참조하세요.

IDE에서 작업할 때 GitHub Copilot과 가장 자주 상호작용하는 방식은 다음과 같습니다:

| 상호작용 모드 | 📝 설명 | 🎯 적합한 용도 |
| --- | --- | --- |
| **⚡ 인라인 제안** | 입력하는 동안 나타나는 AI 기반 코드 제안으로, 한 줄부터 전체 함수까지 컨텍스트 인식 완성을 제공합니다. | 현재 줄의 완성, 때로는 완전히 새로운 코드 블록 |
| **💭 인라인 채팅** | 현재 파일이나 선택 영역에 한정된 대화형 채팅입니다. 특정 코드 블록에 대해 질문할 수 있습니다. | 코드 설명, 특정 함수 디버깅, 타겟 개선 |
| **💬 Ask 모드** | 코드베이스, 코딩, 일반 기술 개념에 대한 질문에 답하도록 최적화되어 있습니다. | 코드 작동 방식 이해, 아이디어 브레인스토밍, 질문하기 |
| **🤖 Agent 모드** | 대부분의 코딩 작업에 권장되는 기본 모드: 자율적 편집, 도구 사용, 작업 완료까지 수행합니다. | 범위가 정해진 수정부터 대규모 다중 파일 구현 작업까지 일상적인 코딩 작업 |
| **🧭 Plan Agent** | 코드를 변경하기 전에 계획을 수립하고 명확한 질문을 하도록 최적화되어 있습니다. | 먼저 검토된 계획을 원할 때, 그 다음 구현으로 넘기기 |

작업하다 보면 GitHub Copilot이 `github.com` 웹사이트와 VS Code, JetBrains, Xcode 등 선호하는 코딩 환경 곳곳에서 도움을 줄 수 있다는 것을 알게 될 것입니다!

오늘의 코딩에서는 [GitHub Codespace](https://github.com/features/codespaces)라고 알려진 사전 구성된 개발 환경에서 VS Code로 실습합니다.

> [!TIP]
> 현재 및 향후 기능에 대해서는 [GitHub Copilot 기능](https://docs.github.com/en/copilot/about-github-copilot/github-copilot-features) 문서에서 자세히 알아볼 수 있습니다.

### :keyboard: Activity: Copilot Chat으로 프로젝트 소개 받기

개발 환경을 시작하고, Copilot을 사용하여 프로젝트에 대해 조금 배운 다음, 테스트 실행을 해봅시다.

1. 아래 버튼을 사용하여 새 탭에서 **Codespace 생성** 페이지를 엽니다. 기본 구성을 사용하세요.

   [![GitHub Codespaces에서 열기](https://github.com/codespaces/badge.svg)](https://codespaces.new/{{full_repo_name}}?quickstart=1)

1. **Repository** 필드가 원본이 아닌 여러분의 실습 복사본인지 확인한 후, 녹색 **Create Codespace** 버튼을 클릭합니다.
   - ✅ 여러분의 복사본: `/{{full_repo_name}}`
   - ❌ 원본: `/skills-kr/getting-started-with-github-copilot`

1. Visual Studio Code가 브라우저에 로드될 때까지 잠시 기다립니다.

1. 왼쪽 사이드바에서 확장 탭을 클릭하고 `GitHub Copilot`과 `Python` 확장이 설치되어 활성화되어 있는지 확인합니다.

   <img width="350" alt="VS Code용 Copilot 확장" src="https://raw.githubusercontent.com/skills-kr/getting-started-with-github-copilot/main/.github/images/copilot-extension-vscode.png" />

   <img width="350" alt="VS Code용 Python 확장" src="https://raw.githubusercontent.com/skills-kr/getting-started-with-github-copilot/main/.github/images/python-extension-vscode.png" />

1. VS Code 상단에서 **Toggle Chat 아이콘**을 찾아 클릭하여 Copilot Chat 사이드 패널을 엽니다.

   <img width="150" alt="image" src="https://raw.githubusercontent.com/skills-kr/getting-started-with-github-copilot/main/.github/images/toggle-chat-icon.png" />

   > 🪧 **참고:** GitHub Copilot을 처음 사용하는 경우 계속하려면 사용 약관에 동의해야 합니다.

1. 첫 번째 상호작용을 위해 **Ask 모드**로 설정되어 있는지 확인합니다.

   <img width="350" alt="Copilot Chat에서 Ask 모드 선택 스크린샷" src="https://raw.githubusercontent.com/skills-kr/getting-started-with-github-copilot/main/.github/images/ask-mode-selection.png" />

1. 아래 프롬프트를 입력하여 Copilot에게 프로젝트를 소개해 달라고 요청합니다.

   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > @workspace Please briefly explain the structure of this project.
   > What should I do to run it?
   > ```

   > 🪧 **참고:** Copilot의 권장 지침을 따를 필요는 없습니다. 이미 환경이 준비되어 있습니다.

   <details>
   <summary>@workspace란 무엇인가요?</summary>

   좋은 질문입니다! 이것은 프로젝트 저장소를 탐색하고 관련 추가 컨텍스트를 포함하려고 시도하는 특수한 [채팅 참여자](https://docs.github.com/en/copilot/using-github-copilot/copilot-chat/github-copilot-chat-cheat-sheet?tool=vscode#chat-participants)입니다.

   </details>

1. 이제 프로젝트에 대해 조금 더 알게 되었으니, 실제로 실행해 봅시다! 왼쪽 사이드바에서 `Run and Debug` 탭을 선택한 다음 **Start Debugging** 아이콘을 누릅니다.

   <img width="300" alt="image" src="https://raw.githubusercontent.com/skills-kr/getting-started-with-github-copilot/main/.github/images/run-and-debug-tab.png" />

1. 웹페이지가 브라우저에서 실행되는 것을 확인하기 위해 URL과 포트를 찾아봅시다. 보이지 않으면 하단 패널을 확장하고 **Ports** 탭을 선택합니다.

1. 목록에서 포트 `8000`과 관련 링크를 찾습니다. 링크 위에 마우스를 올리고 **Open in browser** 아이콘을 선택합니다.

   ![image](https://raw.githubusercontent.com/skills-kr/getting-started-with-github-copilot/main/.github/images/open-in-browser-icon.png)

### :keyboard: Activity: Copilot으로 터미널 명령어 기억하기 🙋

잘 하셨습니다! 이제 앱에 익숙해졌고 작동하는 것을 확인했으니, 커스터마이징을 위한 브랜치를 시작하기 위해 Copilot에게 도움을 요청해 봅시다.

1. VS Code 하단 패널에서 **Terminal** 탭을 선택하고 오른쪽의 플러스 `+` 기호를 클릭하여 새 터미널 창을 만듭니다.

   > 🪧 **참고:** 이렇게 하면 웹 애플리케이션 서비스를 호스팅하는 기존 디버그 세션이 중단되지 않습니다.

1. 새 터미널 창에서 키보드 단축키 `Ctrl + I` (Windows) 또는 `Cmd + I` (Mac)를 사용하여 **Copilot의 터미널 인라인 채팅**을 불러옵니다.

1. Copilot에게 잊어버린 명령어를 기억할 수 있도록 도움을 요청합시다: 브랜치를 만들고 게시하는 방법입니다.

   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > Hey copilot, how can I create and publish a new Git branch called "accelerate-with-copilot"?
   > ```

   > 💡 **팁:** Copilot이 원하는 결과를 제공하지 않으면 언제든지 추가 설명을 계속할 수 있습니다. Copilot은 후속 응답을 위해 대화 기록을 기억합니다.

1. `Run` 버튼을 눌러 Copilot이 터미널 명령어를 삽입하도록 합니다. 복사하여 붙여넣을 필요가 없습니다!

1. 잠시 후 VS Code 하단 상태 바 왼쪽에서 활성 브랜치를 확인합니다. 이제 `accelerate-with-copilot`이라고 표시되어야 합니다. 그렇다면 이 단계는 완료입니다!

1. 이제 브랜치가 GitHub에 푸시되었으므로, Mona가 이미 여러분의 작업을 확인하고 있을 것입니다. 잠시 기다리며 댓글을 주시하세요. Mona가 진행 정보와 다음 레슨으로 응답할 것입니다.

<details>
<summary>문제가 있나요? 🤷</summary><br/>

피드백을 받지 못하는 경우 다음을 확인하세요:

- 정확히 `accelerate-with-copilot`이라는 이름으로 브랜치를 만들었는지 확인하세요. 접두사나 접미사 없이.
- 브랜치가 실제로 저장소에 게시되었는지 확인하세요.

</details>
