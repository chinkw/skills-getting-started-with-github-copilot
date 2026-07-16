## Step 2: Copilot으로 작업하기

이전 단계에서 GitHub Copilot이 프로젝트에 온보딩하는 데 도움을 줄 수 있었습니다. 그것만으로도 엄청난 시간 절약이지만, 이제 실제 작업을 해봅시다!

:bug: **웹사이트에 버그가 있습니다** :bug:

가입 흐름에 문제가 있다는 것을 발견했습니다.
학생들이 현재 같은 활동에 **두 번 이상** 등록할 수 있습니다! Copilot이 원인을 파악하고 깔끔한 수정 방법을 만드는 데 얼마나 도움이 되는지 확인해 봅시다.

시작하기 전에, Copilot 작동 방식에 대한 간단한 입문서입니다. 🧑‍🚀

### 📖 이론: Copilot 작동 방식

간단히 말해, Copilot을 매우 전문적인 동료라고 생각할 수 있습니다. 효과적으로 활용하려면 배경(컨텍스트)과 명확한 방향(프롬프트)을 제공해야 합니다. 또한, 사람마다 고유한 경험(모델)으로 인해 다른 것에 뛰어납니다.

- **컨텍스트를 어떻게 제공하나요?:** 코딩 환경에서 Copilot은 현재 열려있는 코드와 탭을 자동으로 고려합니다. 채팅을 사용하는 경우 명시적으로 파일을 참조할 수도 있습니다.

- **어떤 모델을 선택해야 하나요?:** 이 실습에서는 크게 중요하지 않습니다. 다른 모델을 실험하는 것도 재미의 일부입니다! 그것은 또 다른 레슨이죠! 🤖

- **프롬프트는 어떻게 만드나요?:** 명시적이고 명확하게 작성하면 Copilot이 최선의 결과를 제공합니다. 하지만 일부 전통적인 시스템과 달리, 후속 프롬프트로 언제든지 방향을 명확히 할 수 있습니다.

> [!TIP]
> Copilot의 지식과 기능을 보완하는 여러 가지 다른 방법이 있습니다. [채팅 참여자](https://docs.github.com/en/copilot/using-github-copilot/copilot-chat/github-copilot-chat-cheat-sheet?tool=vscode#chat-participants), [채팅 변수](https://docs.github.com/en/copilot/using-github-copilot/copilot-chat/github-copilot-chat-cheat-sheet?tool=vscode#chat-variables), [슬래시 명령어](https://docs.github.com/en/copilot/using-github-copilot/copilot-chat/github-copilot-chat-cheat-sheet?tool=vscode#slash-commands-1), [MCP 도구](https://code.visualstudio.com/docs/copilot/chat/mcp-servers) 등이 있습니다.

### :keyboard: Activity: Copilot으로 등록 버그 수정하기 :bug:

1. Copilot에게 버그의 원인을 추측하도록 요청해 봅시다. **Copilot Chat** 패널을 **Ask 모드**로 열고 다음을 입력합니다.

   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > @workspace Students are able to register twice for an activity.
   > Where could this bug be coming from?
   > ```

1. 이제 문제가 `src/app.py` 파일의 `signup_for_activity` 메서드에 있다는 것을 알았으니, Copilot의 권장 사항을 따라 (반수동으로) 수정해 봅시다. 주석으로 시작하고 Copilot이 수정을 완성하도록 합니다.
   1. `src/app.py` 파일을 엽니다.

      > 💡 **팁:** Copilot이 채팅에서 `src/app.py`를 언급했다면, 채팅 뷰에서 파일을 직접 클릭하여 열 수 있습니다.

   1. 파일 하단 근처에서 `signup_for_activity` 함수를 찾습니다.

   1. 학생 추가를 설명하는 주석 줄을 찾습니다. 그 위가 등록 확인을 하기에 논리적인 위치입니다.

   1. 아래 주석을 입력하고 Enter를 눌러 다음 줄로 이동합니다. 잠시 후 Copilot의 제안이 임시 그림자 텍스트로 나타납니다! 멋지죠! :tada:

      주석:

      ```python
      # Validate student is not already signed up
      ```

      <img width="700" alt="편집기에서 Copilot 그림자 텍스트 제안" src="https://raw.githubusercontent.com/skills-kr/getting-started-with-github-copilot/main/.github/images/shadow-text.gif" />

   1. `Tab`을 눌러 Copilot의 제안을 수락하고 그림자 텍스트를 코드로 변환합니다.

   <details>
   <summary>예시 결과</summary><br/>

   Copilot은 나날이 발전하고 있으며 항상 같은 결과를 생성하지는 않을 수 있습니다. 제안이 마음에 들지 않으면, 이 실습을 만들 때 생성한 유효한 제안 결과의 예시를 사용하여 계속 진행할 수 있습니다.

   ```python
   @app.post("/activities/{activity_name}/signup")
   def signup_for_activity(activity_name: str, email: str):
      \"\"\"Sign up a student for an activity\"\"\"
      # Validate activity exists
      if activity_name not in activities:
         raise HTTPException(status_code=404, detail="Activity not found")

      # Get the activity
      activity = activities[activity_name]

      # Validate student is not already signed up
      if email in activity["participants"]:
        raise HTTPException(status_code=400, detail="Student is already signed up")

      # Add student
      activity["participants"].append(email)
      return {"message": f"Signed up {email} for {activity_name}"}
   ```

   </details>

### :keyboard: Activity: Copilot으로 샘플 데이터 생성하기 📋

새로운 프로젝트 개발에서는 테스트를 위해 실제처럼 보이는 가짜 데이터가 있으면 유용합니다. Copilot은 이런 작업에 뛰어나므로, 더 많은 샘플 활동을 추가하고 Copilot과 상호작용하는 또 다른 방법인 **인라인 채팅**을 소개합시다.

**인라인 채팅**과 **Copilot Chat** 패널은 비슷하지만 범위가 다릅니다: Copilot Chat은 더 넓은 범위의 다중 파일 또는 탐색적 질문을 처리하고, 인라인 채팅은 바로 앞에 있는 정확한 줄이나 블록에 대한 타겟 도움이 필요할 때 더 빠릅니다.

1. `src/app.py` 파일 상단 근처(약 23번째 줄)에서 예시 과외 활동이 구성된 `activities` 변수를 찾습니다.

1. 사전의 처음부터 끝까지 마우스를 클릭하고 드래그하여 전체 `activities` 딕셔너리를 하이라이트합니다. 이것은 다음 프롬프트에 대한 컨텍스트를 Copilot에 제공하는 데 도움이 됩니다.

   <img width="700" alt="인라인 채팅을 열기 전에 하이라이트된 activities 딕셔너리" src="https://raw.githubusercontent.com/skills-kr/getting-started-with-github-copilot/main/.github/images/activities-dict-highlighted.png" />

1. 키보드 명령 `Ctrl + I` (Windows) 또는 `Cmd + I` (Mac)를 사용하여 Copilot 인라인 채팅을 불러옵니다.

   > 💡 **팁:** Copilot 인라인 채팅을 불러오는 또 다른 방법: 선택한 줄에서 `우클릭` -> `Open Inline Chat`.

1. 아래 프롬프트 텍스트를 입력하고 Enter 또는 오른쪽의 **Send** 버튼을 누릅니다.

   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > Add 2 more sports related activities, 2 more artistic
   > activities, and 2 more intellectual activities.
   > ```

1. 잠시 후 Copilot이 코드를 직접 변경하기 시작합니다. 변경 사항은 추가와 삭제를 쉽게 식별할 수 있도록 다른 스타일로 표시됩니다. 잠시 시간을 들여 변경 사항을 검사하고 확인한 다음 **Keep** 버튼을 누릅니다.

   <details>
   <summary>예시 결과</summary><br/>

   Copilot은 나날이 발전하고 있으며 항상 같은 결과를 생성하지는 않을 수 있습니다. 제안이 마음에 들지 않으면, 이 실습을 만들 때 생성한 예시 결과를 사용하여 문제가 있는 경우 계속 진행할 수 있습니다.

   ```python
   # In-memory activity database
   activities = {
      "Chess Club": {
         "description": "Learn strategies and compete in chess tournaments",
         "schedule": "Fridays, 3:30 PM - 5:00 PM",
         "max_participants": 12,
         "participants": ["michael@mergington.edu", "daniel@mergington.edu"]
      },
      "Programming Class": {
         "description": "Learn programming fundamentals and build software projects",
         "schedule": "Tuesdays and Thursdays, 3:30 PM - 4:30 PM",
         "max_participants": 20,
         "participants": ["emma@mergington.edu", "sophia@mergington.edu"]
      },
      "Gym Class": {
         "description": "Physical education and sports activities",
         "schedule": "Mondays, Wednesdays, Fridays, 2:00 PM - 3:00 PM",
         "max_participants": 30,
         "participants": ["john@mergington.edu", "olivia@mergington.edu"]
      },
      "Basketball Team": {
         "description": "Competitive basketball training and games",
         "schedule": "Tuesdays and Thursdays, 4:00 PM - 6:00 PM",
         "max_participants": 15,
         "participants": []
      },
      "Swimming Club": {
         "description": "Swimming training and water sports",
         "schedule": "Mondays and Wednesdays, 3:30 PM - 5:00 PM",
         "max_participants": 20,
         "participants": []
      },
      "Art Studio": {
         "description": "Express creativity through painting and drawing",
         "schedule": "Wednesdays, 3:30 PM - 5:00 PM",
         "max_participants": 15,
         "participants": []
      },
      "Drama Club": {
         "description": "Theater arts and performance training",
         "schedule": "Tuesdays, 4:00 PM - 6:00 PM",
         "max_participants": 25,
         "participants": []
      },
      "Debate Team": {
         "description": "Learn public speaking and argumentation skills",
         "schedule": "Thursdays, 3:30 PM - 5:00 PM",
         "max_participants": 16,
         "participants": []
      },
      "Science Club": {
         "description": "Hands-on experiments and scientific exploration",
         "schedule": "Fridays, 3:30 PM - 5:00 PM",
         "max_participants": 20,
         "participants": []
      }
   }
   ```

   </details>

1. 이제 웹사이트로 가서 새 활동이 표시되는지 확인할 수 있습니다.

### :keyboard: Activity: Copilot으로 작업 설명하기 💬

버그를 수정하고 예시 활동을 확장하는 훌륭한 작업을 하셨습니다! 이제 Copilot의 도움을 받아 작업을 커밋하고 GitHub에 푸시합시다!

1. 왼쪽 사이드바에서 `Source Control` 탭을 선택합니다.

   > 💡 **팁:** 소스 컨트롤 영역에서 파일을 열면 단순히 여는 것이 아니라 원본과의 차이점이 표시됩니다.

1. `app.py` 파일을 찾고 `+` 기호를 눌러 변경 사항을 스테이징 영역에 모읍니다.

   ![image](https://raw.githubusercontent.com/skills-kr/getting-started-with-github-copilot/main/.github/images/staging-changes-icon.png)

1. 스테이징된 변경 사항 목록 위에서 **Message** 텍스트 박스를 찾되, 지금은 **아무것도 입력하지 마세요**.
   - 일반적으로 여기에 변경 사항에 대한 짧은 설명을 작성하지만, 이제 Copilot이 도와줍니다!

1. **Message** 텍스트 박스 오른쪽에서 **Generate Commit Message** 버튼(반짝이 아이콘)을 찾아 클릭합니다.

1. **Commit** 버튼과 **Sync Changes** 버튼을 눌러 변경 사항을 GitHub에 푸시합니다.

1. Mona가 작업을 확인하고 피드백을 제공하며 다음 레슨을 공유할 때까지 잠시 기다립니다.

<details>
<summary>문제가 있나요? 🤷</summary><br/>

피드백을 받지 못하는 경우 다음을 확인하세요:

- `accelerate-with-copilot` 브랜치에 `src/app.py` 파일 변경 사항을 푸시했는지 확인하세요.

</details>
