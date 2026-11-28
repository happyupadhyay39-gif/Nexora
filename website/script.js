document.addEventListener("DOMContentLoaded", function () {
    const navbar = document.querySelector(".site-navbar");
    const navigation = document.getElementById("mainNavigation");
    const navigationLinks = Array.from(document.querySelectorAll(".navbar-nav .nav-link"));
    const anchorLinks = document.querySelectorAll('a[href^="#"]');
    const sections = navigationLinks
        .map(function (link) {
            return document.querySelector(link.getAttribute("href"));
        })
        .filter(Boolean);

    document.documentElement.classList.add("js-enabled");

    function updateNavbar() {
        navbar.classList.toggle("is-scrolled", window.scrollY > 24);
    }

    updateNavbar();
    window.addEventListener("scroll", updateNavbar, { passive: true });

    anchorLinks.forEach(function (link) {
        link.addEventListener("click", function (event) {
            const target = document.querySelector(link.getAttribute("href"));
            if (!target) {
                return;
            }

            event.preventDefault();
            target.scrollIntoView({ behavior: "smooth", block: "start" });

            if (window.innerWidth < 992 && navigation.classList.contains("show") &&
                window.bootstrap && window.bootstrap.Collapse) {
                window.bootstrap.Collapse.getOrCreateInstance(navigation).hide();
            }
        });
    });

    if ("IntersectionObserver" in window) {
        const revealObserver = new IntersectionObserver(function (entries, observer) {
            entries.forEach(function (entry) {
                if (entry.isIntersecting) {
                    entry.target.classList.add("is-visible");
                    observer.unobserve(entry.target);
                }
            });
        }, { threshold: 0.12 });

        document.querySelectorAll(".reveal").forEach(function (element) {
            revealObserver.observe(element);
        });

        const sectionObserver = new IntersectionObserver(function (entries) {
            entries.forEach(function (entry) {
                if (!entry.isIntersecting) {
                    return;
                }

                navigationLinks.forEach(function (link) {
                    const isCurrent = link.getAttribute("href") === "#" + entry.target.id;
                    link.classList.toggle("active", isCurrent);
                    if (isCurrent) {
                        link.setAttribute("aria-current", "location");
                    } else {
                        link.removeAttribute("aria-current");
                    }
                });
            });
        }, { rootMargin: "-25% 0px -65% 0px" });

        sections.forEach(function (section) {
            sectionObserver.observe(section);
        });
    } else {
        document.querySelectorAll(".reveal").forEach(function (element) {
            element.classList.add("is-visible");
        });
    }
});
