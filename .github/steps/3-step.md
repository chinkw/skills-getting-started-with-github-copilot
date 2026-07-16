## Step 3: 하이퍼드라이브 가동 - Copilot Agent 모드 🚀

### 📖 이론: Copilot Agent 모드란?

Copilot [Agent 모드](https://code.visualstudio.com/docs/copilot/chat/chat-agent-mode)는 AI 지원 코딩의 차세대 진화입니다. 자율적인 동료 프로그래머로서 여러분의 명령에 따라 다단계 코딩 작업을 수행합니다.

Copilot Agent 모드는 컴파일 및 린트 오류에 반응하고, 터미널 및 테스트 출력을 모니터링하며, 작업이 완료될 때까지 루프에서 자동 수정합니다.

#### Agent 모드 (한눈에 보기)

| 측면 | 👩‍🚀 Agent 모드 |
| --- | --- |
| 자율성과 계획 | 높은 수준의 요청을 다단계 작업으로 분해하고 작업이 완료될 때까지 반복합니다. |
| 컨텍스트 수집 | 현재 컨텍스트를 사용하고 필요할 때 추가 관련 파일을 찾을 수 있습니다. |
| 도구 사용 | 도구를 자동으로 선택하고 호출합니다. `#codebase`와 같은 멘션으로 도구를 지시할 수도 있습니다. |
| 승인 및 안전 게이트 | 민감한 작업은 실행 전에 승인을 요구할 수 있어 제어를 유지할 수 있습니다. |

#### 🧰 Agent 모드 도구

Agent 모드는 사용자 요청을 처리하는 동안 전문화된 작업을 수행하기 위해 도구를 사용합니다. 이러한 작업의 예시:

- 프롬프트를 완성하기 위한 관련 파일 찾기
- 웹페이지 내용 가져오기
- 테스트 또는 터미널 명령 실행

> [!TIP]
> VS Code는 많은 내장 도구를 제공하지만, **MCP 도구**를 통해 Agent 모드에 더 많은 도메인 특화 기능을 제공할 수도 있습니다.
>
> [MCP 서버](https://code.visualstudio.com/docs/copilot/customization/mcp-servers) 및 [GitHub MCP Server](https://github.com/github/github-mcp-server)에 대해 자세히 알아보세요.

이제 **Agent 모드**를 사용해 봅시다! 👩‍🚀

### :keyboard: Activity: Copilot으로 새 기능 추가하기! :rocket:

웹사이트에 활동 목록이 있지만, 참가자 목록은 비밀로 되어 있습니다 🤫

Copilot을 사용하여 각 활동 아래에 등록된 학생을 표시하도록 웹사이트를 변경합시다!

1. Copilot Chat 창 하단에서 드롭다운을 사용하여 **Agent** 모드로 전환합니다.

   <img width="350" alt="image" src="https://raw.githubusercontent.com/skills-kr/getting-started-with-github-copilot/main/.github/images/agent-mode-dropdown.png" />

1. 웹페이지와 관련된 파일을 열고 각 편집기 창(또는 파일)을 채팅 패널로 끌어다 놓아 Copilot에게 컨텍스트로 사용하도록 알립니다.

   - `src/static/app.js`
   - `src/static/index.html`
   - `src/static/styles.css`

   > 🪧 **참고:** 파일을 컨텍스트로 추가하는 것은 선택 사항입니다. 건너뛰더라도 Copilot Agent 모드는 `#codebase`와 같은 도구를 사용하여 프롬프트에서 관련 파일을 검색할 수 있습니다. 특정 파일을 추가하면 Copilot을 올바른 방향으로 안내하는 데 도움이 되며, 특히 큰 코드베이스에서 유용합니다.

   <img width="400" alt="컨텍스트에 추가된 파일을 보여주는 이미지" src="https://raw.githubusercontent.com/skills-kr/getting-started-with-github-copilot/main/.github/images/files-added-to-context.png" />

   > 💡 **팁:** **Add Context...** 버튼을 사용하여 GitHub 이슈나 터미널 창의 결과와 같은 다른 컨텍스트 항목을 제공할 수도 있습니다.

1. Copilot에게 활동의 현재 참가자를 표시하도록 프로젝트를 업데이트하도록 요청합니다. 편집 제안이 도착하고 적용될 때까지 잠시 기다립니다.

   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > Hey Copilot, can you please edit the activity cards to add a participants section.
   > It will show what participants that are already signed up for that activity as a bulleted list.
   > Remember to make it pretty!
   > ```

   Copilot이 작업을 마치면, 어떤 변경 사항을 유지할지는 여러분이 결정합니다.

   아래에 표시된 **Keep** 버튼을 사용하여 모든 변경 사항을 수락/취소하거나 변경 사항별로 검토하고 결정할 수 있습니다. 이는 채팅 패널 뷰에서 또는 편집된 각 파일을 검사하면서 수행할 수 있습니다.

      <img width="900" alt="변경 사항을 유지하거나 취소하는 버튼" src="https://raw.githubusercontent.com/skills-kr/getting-started-with-github-copilot/main/.github/images/review-changes-buttons.png" />

1. 변경 사항을 단순히 수락하기 전에, 웹사이트를 다시 확인하고 모든 것이 예상대로 업데이트되었는지 확인하세요.

   다음은 업데이트된 활동 카드의 예시입니다. 앱을 다시 시작하거나 페이지를 새로고침해야 할 수 있습니다.

   <img width="350" alt="참가자 정보가 있는 활동 카드" src="https://raw.githubusercontent.com/skills-kr/getting-started-with-github-copilot/main/.github/images/activity-card-with-participants.png" />

   > 🪧 **참고:** 여러분의 활동 카드는 다르게 보일 수 있습니다. Copilot이 항상 같은 결과를 생성하지는 않습니다.

   <details>
   <summary>도움이 필요하신가요? 🤷</summary><br/>
   웹사이트가 로드되지 않는 경우 다음을 확인하세요.

   - VS Code 디버거를 다시 시작하여 최신 버전의 웹사이트가 제공되는지 확인하세요.
   - URL을 잊었거나 창을 닫은 경우 Step 1을 다시 확인하세요.
   - 웹페이지를 강제 새로고침하거나 프라이빗 창에서 열어 새로운 복사본을 다운로드해 보세요.

   </details>

1. 변경 사항이 좋다는 것을 확인했으면, 패널을 사용하여 제안된 각 편집을 순환하고 **Keep**을 눌러 변경 사항을 적용합니다.

   > 💡 **팁:** 변경 사항을 직접 수락하거나, 수정하거나, 채팅 인터페이스를 사용하여 추가 지시를 제공하여 개선할 수 있습니다.

### :keyboard: Activity: Agent 모드로 기능적인 "등록 취소" 버튼 추가하기

더 개방적인 요청으로 웹 애플리케이션에 더 많은 기능을 추가하는 실험을 해봅시다.

원하는 결과를 얻지 못하면 다른 모델을 시도하거나 후속 피드백을 제공하여 결과를 개선할 수 있습니다.

1. Copilot이 여전히 **Agent** 모드인지 확인합니다.

   <img width="250" alt="Agent 모드" src="https://raw.githubusercontent.com/skills-kr/getting-started-with-github-copilot/main/.github/images/agent-mode-dropdown.png" />

1. **Tools** 아이콘을 클릭하고 현재 Copilot Agent 모드에서 사용 가능한 모든 도구를 탐색합니다.

   <img width="250" alt="도구 아이콘" src="https://raw.githubusercontent.com/skills-kr/getting-started-with-github-copilot/main/.github/images/tools-icon.png" />

1. 테스트 시간입니다! Copilot에게 참가자 제거 기능을 추가하도록 요청합시다.

   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > #codebase Please add a delete icon next to each participant and hide the bullet points.
   > When clicked, it will unregister that participant from the activity.
   > ```

   `#codebase` 도구는 Copilot이 현재 작업과 관련된 파일, 코드 청크를 찾는 데 사용됩니다.

   > 🪧 **참고:** 이 실습에서는 가장 반복 가능한 결과를 얻기 위해 명시적으로 `#codebase` 도구를 포함합니다.
   > `#codebase` **없이** 프롬프트를 시도하고 Agent 모드가 스스로 더 넓은 프로젝트 컨텍스트를 수집하는지 관찰해 보세요.

1. Copilot이 완료되면, 코드 변경 사항과 웹사이트의 결과를 검사합니다. 결과가 마음에 들면 **Keep** 버튼을 누릅니다. 그렇지 않으면 Copilot에게 피드백을 제공하여 결과를 개선해 보세요.

   > 🪧 **참고:** 웹사이트에서 업데이트를 볼 수 없는 경우 디버거를 다시 시작해야 할 수 있습니다.

1. Copilot에게 등록 버그를 수정하도록 요청합니다.

   > 💡 **팁:** 등록 흐름을 직접 테스트하여 변경 전후의 동작을 명확하게 볼 수 있도록 하는 것이 좋습니다.

   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > I've noticed there seems to be a bug.
   > When a participant is registered, the page must be refreshed to see the change on the activity.
   > ```

1. Copilot이 완료되면, 결과를 검사하고 웹사이트에서 등록 흐름을 검증합니다.

   결과가 마음에 들면 **Keep** 버튼을 누릅니다. 그렇지 않으면 Copilot에게 피드백을 제공해 보세요.

1. 모든 변경 사항을 `accelerate-with-copilot` 브랜치에 **커밋**하고 **푸시**합니다.

1. Mona가 작업을 확인하고 다음 단계를 공유할 때까지 기다립니다.
