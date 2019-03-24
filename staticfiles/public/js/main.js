/* RESPONSIVE ACTIONS */

(function (className) {
    document.addEventListener("DOMContentLoaded", function (event) {
        var elements = document.querySelectorAll(className);
        var elementsArr = Array.prototype.slice.call(elements);

        elementsArr.forEach(function (node) {

            var dot1 = document.createElement('div')
            var dot2 = document.createElement('div')
            var dot3 = document.createElement('div')

            dot1.className = 'gh-button-open-responsive-actions__dot1'
            dot2.className = 'gh-button-open-responsive-actions__dot2'
            dot3.className = 'gh-button-open-responsive-actions__dot3'

            var menu = document.createElement('div')
            menu.appendChild(dot1)
            menu.appendChild(dot2)
            menu.appendChild(dot3)

            if ('onclick' in window) {
                menu.addEventListener('click', function () {
                    node.className = node.className == 'gh-card-action show-mobile' ? 'gh-card-action' : 'gh-card-action show-mobile'
                }, false)
            } else {
                menu.addEventListener('touchstart', function () {
                    node.className = node.className == 'gh-card-action show-mobile' ? 'gh-card-action' : 'gh-card-action show-mobile'
                }, false)
            }

            node.parentNode.insertBefore(menu, node)
            menu.className = "gh-button-open-responsive-actions"
        });

    });

})('.gh-card-action');

/* RESPONSIVE TABLE */
(function (className) {
    document.addEventListener("DOMContentLoaded", function (event) {
        var elements = document.querySelectorAll(className);
        var elementsArr = Array.prototype.slice.call(elements);
        elementsArr.forEach(function (node) {
            var titles = []
            var thArr = Array.prototype.slice.call(node.querySelectorAll('th'));
            thArr.forEach(function (th) {
                titles.push(th.innerText)
            })

            var trArr = Array.prototype.slice.call(node.querySelectorAll('tbody tr'));
            trArr.forEach(function (tr) {
                var tdArr = Array.prototype.slice.call(tr.querySelectorAll('td'));
                tdArr.forEach(function (td, i) {
                    var span = document.createElement('span')
                    span.className = 'gh-table-responsive-title'
                    span.innerText = titles[i]

                    td.insertBefore(span, td.firstChild);
                })
            })
        })
    });



})('.gh-table-responsive');

var clickOutSide = function (inCont, options) {
    var action = function (evt, inContAct, optionsAct) {
        const flyoutElement = inContAct
        let targetElement = evt.target; // clicked element

        do {
            if (targetElement == flyoutElement) {
                // This is a click inside. Do nothing, just return.
                options.inside()
                return;
            }
            // Go up the DOM
            targetElement = targetElement.parentNode;
        } while (targetElement);

        // This is a click outside.
        optionsAct.outside();
    }

    if ('onclick' in window) {
        document.addEventListener('click', function (evt) {
            action(evt, inCont, options)
        }, false)
    } else {
        document.addEventListener('touchstart', function (evt) {
            action(evt, inCont, options)
        }, false)
    }
}

/** SMART SELECT */
var makeSmartSelect = function (optionsConfiguration) {
  
    var type = document.querySelector(optionsConfiguration.id)
    if (!type) return;
    var prevObj = { id: type.dataset.id, label: type.dataset.label }
    var inCont = document.createElement('div')
    inCont.className = 'smart-select'

    inCont.style.position = 'relative'
    var input = document.createElement('input')
    input.className = 'smart-select__input form-control'

    var inputHidden = document.createElement('input')
    var options = document.createElement('ul')
    options.className = 'drop'
    options.style.display = 'none'

    inCont.appendChild(input)
    inCont.appendChild(inputHidden)
    inCont.appendChild(options)

    // inputHidden.style.display = 'none'
    inputHidden.className = 'hidden'
    inputHidden.id = "id_" + optionsConfiguration.key
    inputHidden.name = optionsConfiguration.key
    inputHidden.value = ""
    inputHidden.required = true

    type.appendChild(inCont)


    // si viene data previa, se llena
    if (prevObj.id != null && prevObj.id != '') {
        inputHidden.value = prevObj.id
        input.value = prevObj.label
        input.dataset.value = prevObj.label
    }

    inputHidden.addEventListener('focus', () => {
        inputHidden.blur()
        options.style.display = 'none'
        inCont.focus()
    }, false)

    var asignElementToInput = (event) => {
        const li = event.target;
        const id = li.dataset.id;
        const label = li.dataset.label;
        inputHidden.value = id
        options.innerHTML = "";
        input.value = label
        input.dataset.value = label
    }

    var searchFetch = function (text) {
        fetch(optionsConfiguration.url + text)
            .then(resp => resp.json())
            .then(data => {
                options.innerHTML = "";
                options.style.display = 'block'

                data.forEach(element => {
                    const val = document.createElement('li')
                    val.dataset.id = element.pk
                    val.dataset.label = element.label
                    // val.dataset.sub_type = element.sub_type
                    val.innerText = optionsConfiguration.labelTemplate(element)
                    val.addEventListener('click', asignElementToInput, false)
                    options.appendChild(val)
                });
            })
    }

    input.addEventListener('input', function (self) {
        var val = self.target.value + '';
        if (val.length > 1) {
            searchFetch(self.target.value)
        } else {
            inputHidden.value = ''
            input.dataset.value = ''
        }
        if (input.dataset.value != val) {
            inputHidden.value = ''
        }
    }, false)

    input.addEventListener('click', function (self) {
        var val = self.target.value + '';
        if (val.length > 1) {
            searchFetch(self.target.value)
        }
    }, false)

    clickOutSide(inCont, {
        inside: function () {
            options.style.display = 'block'
            inCont.parentElement.classList.add('smart-select--open');
            inCont.parentElement.classList.remove('smart-select--close');
        },
        outside: function () {
            options.style.display = 'none'
            inCont.parentElement.classList.add('smart-select--close');
            inCont.parentElement.classList.remove('smart-select--open');
        },
    })
};

/* Apply Form Control */
(function () {
    document.addEventListener("DOMContentLoaded", function (event) {
        var elements = document.querySelectorAll('input')
        var elementsArr = Array.prototype.slice.call(elements);
        elementsArr.forEach(function (e) {
            if (
                e.className.search("form-control") === -1
                && e.className.search("hidden") === -1
                && e.className.search('smart-select__input') === -1) {
                e.className = e.className + ' form-control';
                e.parentNode.className = e.parentNode.className + ' form-group'
            }
        });
    });
})();

/* Apply Avatar */
(function () {
    document.addEventListener("DOMContentLoaded", function (event) {
        var elements = document.querySelectorAll('.gh-avatar')
        var elementsArr = Array.prototype.slice.call(elements);
        elementsArr.forEach(function (e) {
            var text = e.dataset.text + '';
            var textList = text.split(' ');
            var isOneWord = textList.length === 1;

            var endText = ''
            if (isOneWord) {
                endText = text.charAt(0);
            } else {
                endText = textList[0].charAt(0) + textList[1].charAt(0);
            }
            e.innerText = endText;
        });
    });
})();