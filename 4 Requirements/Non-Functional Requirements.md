# 3.3 Non-Functional Requirements

# Introduction

**Contents of the section**: This section describes the non-functional requirements that apply to the project. The non-functional requirements focus on the usability requirements.

**Document organization**: The document is divided into 3 sections: the first one indicates the non-functional requirements at the system level, while the other 2 apply to the two groups of functional requirements they’re applied to. Each section is divided into the specific functional requirements the non-functional requirements are attached: The funcional requirement appears as the title of the sub-section, while the non-functional requirement appear as bullet points. The Usability requirements are grouped by the usability factor they belong to. 

# 3.3.1 System Requirements

- ***Non-Functional Requirement 1***: The system shall use the Material Design design system with icons and components from the MaterialUI framework
- ***Non-Functional Requirement 2***: The system shall use the font: Roboto for everything.

# 3.3.2 Authentication and Registration

## 1. The system shall allow the user to register an account with unique credentials within 5 seconds

- **Understandability**:
    - ***Non-Functional Requirement 3***: Notifications of successful account creation shall be clearly visible and understandable.
    - ***Non-Functional Requirement 4***: The account creation form must be understandable/explicit.

## 2. The system shall notify the user if the account was successfully created within 10 seconds after entering their credentials.

- **Understandability**:
    - ***Non-Functional Requirement 5***: Notifications of successful account creation shall be clearly visible and understandable.
- **Engagingness**:
    - ***Non-Functional Requirement 6***: The system must employ visual and auditory cues to confirm unique credentials.

## 3. The system shall notify the user if the account was not successfully created and indicate the reason within 10 seconds after entering their credentials and.

- **Understandability**:
    - ***Non-Functional Requirement 7***: The notification of unsuccessful account creation must indicate the occurred error in a simple and direct way.
- **Engagingness**:
    - ***Non-Functional Requirement 8***: The system must employ visual and auditory cues to indicate if the credentials are not unique.
- **Error Tolerance**:
    - ***Non-Functional Requirement 9***: Notifications of unsuccessful account creation shall provide clear error messages.

## 4. The system shall allow the user to log-in to their account.

- **Understandability**:
    - ***Non-Functional Requirement 10***: The login interface should be simple and aesthetically pleasing according to design guidelines.

## 5. The system shall notify the user if their login was successful within 10 seconds after the credentials are entered.

- **Understandability**:
    - ***Non-Functional Requirement 11***: Success notifications post-login shall be prompt and clear.

## 6. The system shall notify the user if their login failed and indicate the reason within 10 seconds after the credentials were entered.

- **Understandability**:
    - ***Non-Functional Requirement 12***: Failure notifications shall clearly state the problem and suggest corrective actions.

# 3.3.3 Access lessons

**Preconditions**: The user has to be logged-in.

## 1. The system shall allow the user to view their study plan within 10 seconds of logging in.

- **Understandability**:
    - ***Non-Functional Requirement 13***: Viewing the study plan shall be intuitive, with user access times verified to be within 10 seconds of login.

## 2. The system shall allow the user to select a lesson from the study plan (if the lesson is available)

- **Understandability**:
    - ***Non-Functional Requirement 14***: The system should provide visually friendly information about the available lessons using visual aids such as lock icons.

## 3. The system shall present the user with the lesson after 10 seconds of selecting it.

- **Understandability**:
    - ***Non-Functional Requirement 15***: The lesson should have a clear and intuitive layout

## 4. The system shall allow the user to answer the questions on the test within 10 seconds after finishing the lesson.

- **Understandability**:
    - ***Non-Functional Requirement 16***: The questions should have a clear layout that indicates the user how to answer the questions correctly.

## 5. The system shall provide a report with comments on incorrect answers if the user scored less than 100% on the test, within 10 seconds of completing it.

- **Understandability**:
    - ***Non-Functional Requirement 17***: The display of the user's score shall be clear.
    - ***Non-Functional Requirement 18***: The feedback on the incorrect answers shall be clear.

## 6. The system shall allow the user to proceed to the next lesson if they score 70% or higher on the current lesson.

- **Understandability**:
    - ***Non-Functional Requirement 19***: The system shall clearly indicate eligibility to proceed to the next lesson upon achieving a 70% score.
    - ***Non-Functional Requirement 20***: Restrictions on lesson advancement shall be clearly communicated to the user.

## 7. The system shall allow the user to retake the lesson until they score 70% or higher.

- **Understandability**:
    - ***Non-Functional Requirement 21***: The option to re-take the lesson should be clear and intuitive on the lesson selection

## 8. The system shall allow the user to revisit previous lessons.

- **Understandability**:
    - ***Non-Functional Requirement 22***: The system should present lessons that the user can revisit in a friendly manner using visual aids such as arrow icons.

## 9. The system shall prevent the user from accessing lessons beyond their current progress.

- **Understandability**:
    - ***Non-Functional Requirement 23***: The system shall provide visual cues that prevent the user from accessing lessons beyond their current progress, verified through user testing.