Intent:

  -Separate the user interface into three interconnected components: the model, the view and the controller. Let the model manage the data,    the view display the data and the controller mediate updating the data and redrawing the display.

Use the Model-View-Controller pattern when:

  - you want to clearly separate the domain data from its user interface representation
  
Advantages:

- Simultaneous development – Multiple developers can work simultaneously on the model, controller and views.

- High cohesion – MVC enables logical grouping of related actions on a controller together. The views for a specific model are also grouped together.

- Low coupling – The very nature of the MVC framework is such that there is low coupling among models, views or controllers

- Ease of modification – Because of the separation of responsibilities, future development or modification is easier

- Multiple views for a model – Models can have multiple views

Disadvantages:

- Code navigability – The framework navigation can be complex because it introduces new layers of abstraction and requires users to adapt to the decomposition criteria of MVC.

- Multi-artifact consistency – Decomposing a feature into three artifacts causes scattering. Thus, requiring developers to maintain the consistency of multiple representations at once.

- Pronounced learning curve – Knowledge on multiple technologies becomes the norm. Developers using MVC need to be skilled in multiple technologies.
