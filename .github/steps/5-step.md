## Step 5: Pull Request에서 GitHub Copilot 사용하기

축하합니다! 이 실습의 코딩 부분(및 VS Code)은 완료되었습니다. 이제 작업을 머지할 차례입니다. :tada: 마무리로, Pull Request를 빠르게 처리할 수 있는 두 가지 제한 접근 Copilot 기능에 대해 알아봅시다!

### 📖 이론: Pull Request를 위한 GitHub Copilot

#### Copilot Pull Request 요약

일반적으로 노트와 커밋 메시지를 검토한 다음 Pull Request 설명에 요약합니다. 특히 커밋 메시지가 일관적이지 않거나 코드가 잘 문서화되지 않은 경우 시간이 걸릴 수 있습니다. 다행히 Copilot은 Pull Request의 모든 변경 사항을 고려하고 참조와 함께 중요한 하이라이트를 제공할 수 있습니다!

#### Copilot 코드 리뷰

더 많은 눈으로 작업을 검토하는 것은 항상 유용하므로 일반적인 동료 리뷰 프로세스 전에 Copilot에게 첫 번째 검토를 요청합시다. Copilot은 간단한 조정으로 수정할 수 있는 일반적인 실수를 잘 잡아내지만, 책임감 있게 사용하는 것을 기억하세요.

> [!NOTE]
> 이 기능은 **GitHub Copilot**의 유료 플랜에서만 사용할 수 있습니다. [[문서]](https://docs.github.com/en/copilot/get-started/plans)

### :keyboard: Activity: Copilot으로 PR 요약 및 리뷰하기

**Copilot Pull Request 요약**과 **Copilot 코드 리뷰** 모두 접근이 제한되어 있으므로, 이 활동은 대부분 선택 사항입니다. 접근 권한이 없으면 이 활동의 선택 단계를 건너뛰세요.

1. 웹 브라우저에서 다른 탭을 열고 실습 저장소로 이동합니다.

1. 새 Pull Request를 만들라는 **알림 배너**가 표시될 수 있습니다. 그것을 클릭하거나 상단의 **Pull Requests** 탭을 사용하여 **새 Pull Request를 생성**합니다. 다음 세부 정보를 사용하세요:

   - **base:** `main`
   - **compare:** `accelerate-with-copilot`
   - **title:** `Improve student activity registration system`

1. (선택 사항) PR 설명 도구 모음에서 **Copilot** 아이콘과 **Summary** 액션을 클릭합니다. 잠시 후 Copilot이 변경 사항을 기반으로 설명을 추가합니다. :memo:

   <img alt="Copilot 요약 버튼" width="450px" src="https://raw.githubusercontent.com/skills-kr/getting-started-with-github-copilot/main/.github/images/copilot-summarize-button.png">

1. (선택 사항) 오른쪽 정보 패널 상단에서 **Reviewers** 섹션을 찾고 **Copilot 아이콘** 옆의 **Request** 버튼을 클릭합니다. Copilot이 Pull Request에 리뷰 댓글을 추가할 때까지 잠시 기다립니다!

   <img alt="Copilot 리뷰 버튼" width="300px" src="https://raw.githubusercontent.com/skills-kr/getting-started-with-github-copilot/main/.github/images/copilot-review-button.png">

   > 💡 **팁:** Copilot이 리뷰를 요청받았다는 로그 항목을 확인하세요.

1. 하단에서 **Merge pull request** 버튼을 누릅니다. 잘 하셨습니다! 모두 완료되었습니다! :tada:

1. Mona가 작업을 확인하고 피드백을 제공하며 이 실습의 최종 리뷰를 게시할 때까지 잠시 기다립니다!
