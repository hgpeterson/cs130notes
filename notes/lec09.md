# Collaborative Construction Techniques

Previously we saw that test automation is actually not the most effective way of finding software defects.
Design- and code-reviews are much better at finding defects!
These are called *collaborative construction techniques*.

There are many other benefits other than just squashing bugs:
- Peer-pressure = high standard of code quality
- Facilitates knowledge transfer and mentorship
- Fosters healthy team dynamics and a sense of community responsibility

## Code Reviews

**Code reviews** = someone other than the code's author reads and reviews the code. 
Sometimes these are *formal* inspections with an intense acceptance process.
More commonly, these are just *change-based* reviews with lighter-weight "code walk-throughs".

### Benefits
- IBM: every 1 hour of CRs prevented 100 hours of work
- HP: saved $21.5 million per year
- etc.

*Donnie tip:* Try to be the person who gives careful, thoughtful CRs!

### Best practices
- Scope: <60 mins and only 200—400 lines.
- Goals: Reviewers should understand what feedback is being solicited and what background knowledge is needed (check out Google's page: https://google.github.io/eng-practices/review/).
- Feedback: Be courteous, respectful, objective, constructive. Indicate whether your feedback is about a serious issue or just an opinion/suggestion (could preface these by "Nit:").

### Tools

Use **static-analysis tools** to apply coding standards and find common bugs so that the reviewers can focus on the high-level concerns.

Examples in Python:
- Ruff: Style and linting
- Black: Style
- mypy: Type annotations

### Resources

Company guides:
- [Google](https://google.github.io/eng-practices/review/)
- [Palantir](https://blog.palantir.com/code-review-best-practices-19e02780015f)
- [StackOverflow](https://stackoverflow.blog/2019/09/30/how-to-make-good-code-reviews-better/)

Articles:
- [Atlassian](https://www.atlassian.com/agile/software-development/code-reviews)
- [Perforce](https://www.perforce.com/blog/qac/9-best-practices-for-code-review)

## Pair Programming

In PP, two developers work together actively to write a feature and its tests.

- The **Driver** writes the code
- The **Navigator** observes what the driver is doing, asking/answering questions, evaluating work, pointing out potential pitfalls, etc.

Periodically, the Driver and Navigator switch roles.

Pair programming takes more time to write a program (about 15% more for experienced PPers), but the benefits *far outweigh* this increase in development time!

### Catching Defects

- Two people do better at considering all possible scenarios than one person does.
- Two people can validate an implementation against requirements more effectively.
- "Rubber-duck debugging" (see Adam Blank) is incorporated. 
- Tends to produce higher quality designs:
    - Two people will consider a larger design space.
    - Strengths/weaknesses of each design are explored more deeply.
    - The process of negotiating to a consensus allows trade-offs to be balanced more carefully.

### Improved Satisfaction and Team Dynamics

- Higher individual satisfaction.
- Team members learn to work with each other more effectively.
- Knowledge and skills are distributed more broadly throughout the team.

### Productivity

- Switching between Driver/Navigator roles keeps developers fresher and more engaged throughout the day.
- If one dev is distracted by some external interruption, the other person can get them back up to speed more quickly.

### Issues

- PP requires active focus, communication, and participation from *both* programmers
    - Long periods of silence is a warning sign!
- PP won't work well if:
    - Either participant isn't focused on the task at hand
    - Either participant isn't making an effort to engage in ongoing communication about the task at hand
- Other practices to avoid (in a larger team setting):
    - The same pairs of devs always working together
    - Devs never working on areas they are unfamiliar with
    - Pairing participants with unresolvable personality conflicts 
- Not every part of a program warrants pairing!
    - PP is best when the task is complex and the programmers are unfamiliar with the problem
- Senior devs should pair with junior devs to provide mentoring

### Guidance for Drivers

- Spend time up-front discussing possible design approaches with Navigator
- Make sure you are "thinking out loud" as you program
- After writing code, always spend time brainstorming how to test it
- "Give up the steering wheel" at suitable points!

### Guidance for Navigators

- If you see a possible issue, mention it!
- Consider whether the code's control-flow handles all scenarios correctly and satisfies the requirements
- Feel free to suggest structural/style improvements, as well as possible bugs

### References

[Strengthening the Case for PP](http://sunnyday.mit.edu/16.355/williams.pdf)—Laurie Williams

## Final Thought: The Egoless Programmer

> *". . . most of programming is an attempt to compensate for the strictly limited size of our skulls. The people who are best at programming are the people who realize how small their brains are.  They are humble.  The people who are worst at programming are the people who refuse to accept the fact that their brains aren’t equal to the task.  Their egos keep them from being great programmers. The more you learn to compensate for your small brain, the better a programmer you’ll be.  The more humble you are, the faster you’ll improve."*

—Code Complete 2ed. pg. 821, summarizing a 1972 Turing Award lecture by Edsger Dijkstra

Strive to become an [egoless programmer](https://blog.codinghorror.com/the-ten-commandments-of-egoless-programming/)!
