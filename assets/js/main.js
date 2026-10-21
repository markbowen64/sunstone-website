// Mobile menu
const toggle = document.querySelector(".nav-toggle");
const links = document.getElementById("nav-links");
if (toggle && links) {
  toggle.addEventListener("click", () => {
    const open = links.classList.toggle("open");
    toggle.setAttribute("aria-expanded", String(open));
  });
}

document.querySelectorAll("[data-year]").forEach((el) => (el.textContent = new Date().getFullYear()));

// Bid request form: posts to FormSubmit, which emails the request to the address in the action URL.
const form = document.getElementById("bid-form");
if (form) {
  const status = form.querySelector(".form-status");
  const show = (cls, msg) => { status.className = "form-status " + cls; status.textContent = msg; };

  form.addEventListener("submit", async (e) => {
    e.preventDefault();
    const data = new FormData(form);

    if (!form.action.includes("formsubmit.co")) {
      const lines = [];
      for (const [k, v] of data.entries()) if (!k.startsWith("_") && v) lines.push(`${k.replace(/_/g, " ")}: ${v}`);
      const subject = encodeURIComponent(`Bid request: ${data.get("project_name") || ""}`);
      window.location.href = `mailto:${form.dataset.email}?subject=${subject}&body=${encodeURIComponent(lines.join("\n"))}`;
      show("ok", "Your email app should open with the request filled in. Attach drawings or include a link, then send.");
      return;
    }

    const btn = form.querySelector("button[type=submit]");
    btn.disabled = true;
    try {
      const res = await fetch(form.action, { method: "POST", body: data, headers: { Accept: "application/json" } });
      const json = await res.json().catch(() => ({}));
      if (!res.ok || json.success === "false" || json.success === false) throw new Error();
      form.reset();
      show("ok", "Thanks. We've got your project. An estimator will confirm scope and timing shortly.");
    } catch {
      show("err", `Something went wrong. Please email ${form.dataset.email} instead.`);
    } finally {
      btn.disabled = false;
    }
  });
}
