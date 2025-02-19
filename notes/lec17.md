# Program Usability (Part 2)

## Graphical User Interfaces (GUIs)

GUIs can be very powerful, but it's also easy to make *terrible* GUIs that are very confusing and frustrating to users.

Recall usability goals:

- Help the user learn how to perform tasks

- Help the user perform tasks efficiently

- If reasonable, provide customizable options, or adapt to user behavior

- Reduce the impact of errors and failures

- Doing these things should increase the user's confidence over time

### GUIs Designed by Devs

Common issue: *unnecessary complexity!*
Always ask:

> *"What assumptions does this GUI make?*

Devs often expect too much domain knowledge of the user.
Remember: ETE, HTP.

To streamline an overcomplicated GUI, ask:

- What are the most common operations users need to perform?

- What are the most common config settings that users specify?

    - Are some common config options frequently used together?

    - Are some mutually exclusive?

    - Are some considered "basic" or "advanced"?

    - Are some never used?

### Tabbed Panes

Tabbed panes help manage complexity in a UI. 

- An example of a **UI Metaphor**: A visual appearance and set of behaviors that leverages external knowledge the user already has. Most users are familiar with tabbed folders in filling cabinets, for example.

Can use tabbed panes to:

- Show different kinds of details about an entity

- Group config options into different categories

- Present alternative workflows

The metaphor breaks down when there are too many tabs . . .

**Alternatives** 

- Having a category/sub-category selector on the side (e.g., IntelliJ IDE)

- Having a menu with lots of different icons (e.g., Apple System Preferences)

- Having different UI depending on situation (e.g., Apple calculator)

### The User Model

The user has an internal model of how your GUI "should" work informed by

- How the user thinks they should perform their tasks

- What UI elements you use, and how the user believes they should work

- Other UIs the user has worked with

This may not match the actual behavior of the UI.

- This is where your UI must facilitate learning and allow users to make mistakes without severe consequences

### Facilitate Learning

#### Tooltips

**Hover-over tool tips** are a widely used mechanism for helping users learn how to use the GUI

- Should be brief and add useful info

- More info from the [Neilsen Norman Group](https://www.nngroup.com/articles/tooltip-guidelines/)


#### Wizards

**Wizards** are a useful approach for walking the user through a complex, multi-step operation.
Useful when:

- An operation has multiple, distinct steps

- At each step, the user may need assistance to provide the correct input

- The operation is not very common

Only use wizards where they really help and keep them as simple as possible!

- They can make users feel over-constrained

- Allow for "expert mode" for advanced users

- Allow user to finish the sequence early

**Good example:** MS Excel text-import wizard.

### Choosing and Using UI Components

Avoid using standard UI widgets, gestures, etc. in unusual ways.
**Match standard behaviors for the UI platform you are using.**

- Example: Bringing two fingers together on a touch screen should zoom out.

It's also possible to pick the wrong widget for the task (e.g., radio buttons to select you state rather than a drop-down menu).

### Assumptions about the Mouse

**Assume that users aren't very good at using the mouse (or touchpad).**

- Give users large targets to click on

    - E.g., Large buttons, some fudge-space for small targets

    - **Buddy widgets:** When the user clicks on the label, the GUI automatically transfers focus to its buddy

- Put things on the corners/edges of the screen since they're easiest to get to

**Assume users may not want to use (or may not have) a mouse.**

- Implement keyboard shortcuts for common operations

- Specify the tab-order for your GUIs so that users can tab between UI widgets in a reasonable order (don't force the user to hop back and forth between mouse and keyboard)

**Assume that users don't want to read anything in your GUI.**

- Be as concise as possible

- Use icons for common tasks

### Internationalization (i18n)

**Facilitate internationalization efforts from the start.**

- Example: Use Qt's `tr()` function throughout and from the start

- Leave extra room in your UI for translated text (Italian takes 3x more space than English!)

### Usability Testing

Get real users to test your GUI! For initial designs, use "hallway usability tests":

> *"Find a willing victim, show them your user interface, and see if they can figure out what it is for, how to use it, etc.  Coach them as little as possible for maximum result"* —Joel Spolsky
