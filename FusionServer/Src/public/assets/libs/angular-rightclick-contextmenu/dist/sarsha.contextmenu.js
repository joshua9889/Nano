! function n(e, t, o) {
    function i(s, c) {
        if (!t[s]) {
            if (!e[s]) {
                var l = "function" == typeof require && require;
                if (!c && l) return l(s, !0);
                if (r) return r(s, !0);
                var a = new Error("Cannot find module '" + s + "'");
                throw a.code = "MODULE_NOT_FOUND", a
            }
            var u = t[s] = {
                exports: {}
            };
            e[s][0].call(u.exports, function (n) {
                var t = e[s][1][n];
                return i(t ? t : n)
            }, u, u.exports, n, e, t, o)
        }
        return t[s].exports
    }
    for (var r = "function" == typeof require && require, s = 0; s < o.length; s++) i(o[s]);
    return i
}({
    1: [function (n, e, t) {
        "use strict";
        var o = [],
            i = function (n, e) {
                var t = document.head || document.getElementsByTagName("head")[0],
                    i = o[o.length - 1];
                if (e = e || {}, e.insertAt = e.insertAt || "bottom", "top" === e.insertAt) i ? i.nextSibling ? t.insertBefore(n, i.nextSibling) : t.appendChild(n) : t.insertBefore(n, t.firstChild), o.push(n);
                else {
                    if ("bottom" !== e.insertAt) throw new Error("Invalid value for parameter 'insertAt'. Must be 'top' or 'bottom'.");
                    t.appendChild(n)
                }
            };
        e.exports = {
            createLink: function (n, e) {
                var t = document.head || document.getElementsByTagName("head")[0],
                    o = document.createElement("link");
                o.href = n, o.rel = "stylesheet";
                for (var i in e)
                    if (e.hasOwnProperty(i)) {
                        var r = e[i];
                        o.setAttribute("data-" + i, r)
                    }
                t.appendChild(o)
            },
            createStyle: function (n, e, t) {
                t = t || {};
                var o = document.createElement("style");
                o.type = "text/css";
                for (var r in e)
                    if (e.hasOwnProperty(r)) {
                        var s = e[r];
                        o.setAttribute("data-" + r, s)
                    }
                o.sheet ? (o.innerHTML = n, o.sheet.cssText = n, i(o, {
                    insertAt: t.insertAt
                })) : o.styleSheet ? (i(o, {
                    insertAt: t.insertAt
                }), o.styleSheet.cssText = n) : (o.appendChild(document.createTextNode(n)), i(o, {
                    insertAt: t.insertAt
                }))
            }
        }
    }, {}],
    2: [function (n, e, t) {
        angular.module("contextMenu", []).component("contextMenu", {
            bindings: {
                menuOptions: "<",
                data: "<",
                closeMenu: "&",
                options: "<"
            },
            templateUrl: "src/component/menu.html",
            controller: function () {
                var n = this;
                this.onClick = function (e, t) {
                    n.isOptionDisabled(t) || (n.closeMenu(), t.onClick({
                        option: t,
                        dataContext: n.data
                    }))
                }, this.isOptionDisabled = function (e) {
                    return e.disabled && e.disabled(n.data)
                }
            }
        })
    }, {}],
    3: [function (n, e, t) {
        var o = ".sh_menu_container {\n  position: fixed;\n  height: auto;\n  background: #ececec;\n  z-index: 90001;\n  min-width: 150px;\n  border: 0.5px solid rgba(0,0,0,0.2);\n  border-radius: 2.5px;\n  box-shadow: 0px 0px 10px 2px rgba(0,0,0,0.1);\n}\n.sh_menu_container ul {\n  list-style: none;\n  padding: 5px 0;\n  margin: 0;\n}\n.sh_menu_container ul.sh_menu_rtl {\n  direction: rtl;\n}\n.sh_menu_container ul li {\n  padding-right: 10px;\n  padding-left: 15px;\n  padding-bottom: 5px;\n  padding-top: 5px;\n  transition: all 0.15s;\n}\n.sh_menu_container ul li.sh_menu_item:hover {\n  cursor: pointer;\n  background: #4b8bec;\n  color: white;\n}\n.sh_context_mask {\n  position: fixed;\n  top: 0;\n  bottom: 0;\n  left: 0;\n  right: 0;\n  z-index: 90000;\n}\n.sh_menu_divider {\n  height: 1px;\n  margin: 1px 1px 8px 1px;\n  overflow: hidden;\n  background-color: #ececec;\n  border-bottom: 1px solid #d0d0d0;\n  line-height: 10px;\n}\n.sh_menu_container ul li.sh_menu_disabled {\n  color: #d0d0d0;\n}\n.sh_menu_container ul li.sh_menu_disabled:hover {\n  cursor: not-allowed;\n  color: #d0d0d0;\n  background: #ececec;\n}\n";
        n("browserify-css").createStyle(o, {
            href: "src/component/menu.css"
        }, {
            insertAt: "bottom"
        }), e.exports = o
    }, {
        "browserify-css": 1
    }],
    4: [function (n, e, t) {
        function o(n) {
            return {
                scope: {
                    menuOptions: "<",
                    contextData: "<",
                    options: "<"
                },
                bindToController: !0,
                controllerAs: "$ctrl",
                controller: angular.noop,
                link: function (e, t, o, i) {
                    function r(n, e, t) {
                        var o = n[0].offsetWidth,
                            i = e.clientX;
                        t.rtl && (i -= o), n[0].style.top = e.clientY + "px", n[0].style.left = i + "px"
                    }

                    function s() {
                        var t = angular.element('<context-menu options="$ctrl.options" close-menu="$ctrl.destroyElements()" menu-options="$ctrl.menuOptions" data="$ctrl.contextData" class="sh_menu_container"></context-menu>'),
                            o = n(t),
                            i = o(e);
                        return i
                    }

                    function c() {
                        var n = angular.element('<div class="sh_context_mask"></div>');
                        return n.on("mousedown", function (n) {
                            l()
                        }), n
                    }

                    function l() {
                        a.remove(), u.remove()
                    }
                    var a, u, d = {
                        rtl: !1
                    };
                    i.destroyElements = function () {
                        l()
                    }, i.options = Object.assign({}, d, i.options), t.on("contextmenu", function (n) {
                        n.preventDefault();
                        var e = angular.element(document.body);
                        a = s(), u = c(), e.append(a), e.append(u), r(a, n, i.options)
                    })
                }
            }
        }
        n("./component/menu.component.js"), n("./component/menu.css"), angular.module("shContextMenu", ["contextMenu"]).directive("shContextMenu", o), o.$inject = ["$compile"]
    }, {
        "./component/menu.component.js": 2,
        "./component/menu.css": 3
    }]
}, {}, [4]), angular.module("shContextMenu").run(["$templateCache", function (n) {
    n.put("src/component/menu.html", '<ul ng-class="{sh_menu_rtl: $ctrl.options.rtl}">\n    <li ng-style="" ng-repeat="option in $ctrl.menuOptions" ng-class="{sh_menu_item: !option.divider, sh_menu_divider: option.divider, sh_menu_disabled: $ctrl.isOptionDisabled(option)}">\n        <div ng-click="$ctrl.onClick($event, option)" ng-if="!option.divider">\n            {{option.label}}\n        </div>\n    </li>\n</ul>')
}]);
