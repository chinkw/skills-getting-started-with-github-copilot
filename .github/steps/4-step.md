## Step 4: Planning Agent로 구현 계획 세우기 🧭

지난 단계에서 Agent 모드가 빠르게 움직이고 새로운 기능을 배포하는 데 도움을 주었습니다. 🚀

이제 한 라운드 동안 속도를 늦추고 설계자처럼 작업합시다: 먼저 강력한 테스팅 접근 방식을 정의한 다음 구현을 위해 넘깁니다. 이렇게 하면 더 나은 명확성, 더 적은 놀라움, 더 깨끗한 결과를 얻을 수 있습니다. 🧪

### 📖 이론: Copilot Plan Agent란?

Copilot [Plan Agent](https://code.visualstudio.com/docs/copilot/agents/planning)는 코드를 변경하기 전에 솔루션을 설계하도록 도와줍니다.

바로 편집에 뛰어드는 대신, 요청을 조사하고, 명확한 질문을 하며, 개선할 수 있는 구현 계획 초안을 작성합니다.

#### Plan Agent (한눈에 보기)

| 측면 | 🧭 Plan Agent |
| --- | --- |
| 목적 | 코딩이 시작되기 전에 구조화된 구현 계획을 만듭니다. |
| 컨텍스트 수집 | 읽기 전용 리서치를 사용하여 요구 사항과 제약 조건을 이해합니다. |
| 협업 스타일 | 명확한 질문을 한 다음 답변을 사용하여 계획을 업데이트합니다. |
| 반복 | 구현 전 여러 차례의 개선 패스를 지원합니다. |
| 안전성 | 계획을 승인하고 **Agent 모드**로 넘기기 전까지 파일을 편집하지 않습니다. |
| 핸드오프 | **Start implementation** 버튼이 승인된 계획을 코딩을 위한 **Agent 모드**로 넘깁니다. |

> [!TIP]
> 높은 수준의 요청으로 시작한 다음 후속 프롬프트에서 제약 조건과 세부 사항을 추가할 수 있습니다.

### ⌨️ Activity: 백엔드 테스트 계획 및 구현

백엔드에는 아직 테스트 커버리지가 없습니다. **Plan Agent**를 사용하여 계획을 세우고, 질문에 답하고, 구현을 시작합니다.

1. **Copilot Chat** 패널을 열고 **Plan Agent**로 전환합니다.

   <img width="350" alt="image" src="https://raw.githubusercontent.com/skills-kr/getting-started-with-github-copilot/main/.github/images/plan-mode-dropdown.png" />

1. 넓은 범위의 프롬프트로 시작하면 Copilot이 세부 사항을 채우는 데 도움을 줍니다:

   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > I want to add backend FastAPI tests in a separate tests directory.
   > ```

1. Copilot이 첫 번째 계획을 생성할 때까지 기다립니다. 질문이 있으면 최선을 다해 답변하세요.

   > 🪧 **참고:** 완벽하게 만들 필요는 없습니다. 나중에 언제든지 계획을 개선할 수 있습니다.

1. 후속 프롬프트에서 계획을 개선하고 추가 세부 사항을 제공할 수 있습니다.

   몇 가지 예시:

   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > Let's use the AAA (Arrange-Act-Assert) testing pattern to structure our tests
   > ```

   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > Make sure we use `pytest` and add it to `requirements.txt` file
   > ```

1. 제안된 계획을 검토하고 만족스러우면 **Start implementation**을 클릭하여 **Agent 모드**로 넘깁니다.

   <img width="350" alt="image" src="https://raw.githubusercontent.com/skills-kr/getting-started-with-github-copilot/main/.github/images/plan-mode-start-implementation.png" />

   버튼을 클릭하면 **Plan**에서 **Agent 모드**로 전환된 것을 확인하세요. 이 시점부터 Copilot은 이전과 마찬가지로 코드베이스를 편집할 수 있습니다.

1. Copilot이 방금 만든 계획을 구현하는 것을 지켜봅니다. 특정 도구를 실행하기 위한 권한을 요청할 수 있습니다 (예: 명령 실행 또는 가상 환경 생성). 이러한 권한을 승인하여 계속 작업할 수 있도록 합니다.

1. 변경 사항을 검토하고 테스트가 성공적으로 실행되는지 확인합니다. 필요한 경우 구현이 완료될 때까지 계속 안내합니다.

   **🎯 목표: 다음으로 넘어가기 전에 모든 테스트가 통과(녹색)되어야 합니다. ✅**

   > 🪧 **참고:** Agent 모드가 한 번에 완료할 수도 있고, 여러분의 후속 프롬프트가 필요할 수도 있습니다.

1. 모든 변경 사항을 `accelerate-with-copilot` 브랜치에 **커밋**하고 **푸시**합니다.

1. Mona가 작업을 확인하고 다음 단계를 공유할 때까지 기다립니다.

<details>
<summary>문제가 있나요? 🤷</summary><br/>

- 테스트가 실행되지 않았다면 Copilot에게 실행해 달라고 요청하세요.
- `requirements.txt`에 `pytest`가 추가되어 있고 `tests/` 디렉토리가 존재하는지 확인하세요.

</details>
