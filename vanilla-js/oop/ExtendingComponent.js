//todo - check if you can remove listener

class Tooltip extends Component {
    constructor(closeNotifierFunction) {
      super();
      this.closeNotifier = closeNotifierFunction;
      this.create();
    }
  
    closeTooltip = () => {
      this.detach();
      this.closeNotifier();
    };
  
    create() {
      const tooltipElement = document.createElement('div');
      tooltipElement.className = 'classlist';
      tooltipElement.textContent = 'txt content';
      tooltipElement.addEventListener('click', this.closeTooltip);
      this.element = tooltipElement;
    }
  }