const API_URL = "https://labcalc-online.onrender.com/api";


/* =========================
   LOGIN
========================= */

function login() {

  const usuario = document.getElementById("usuario");
  const senha = document.getElementById("senha");

  if (!usuario || !senha) {
    return;
  }

  if (
    usuario.value.trim() === "" ||
    senha.value.trim() === ""
  ) {

    document.getElementById("resultado_login").innerHTML = `
      <span class="erro">
        Preencha usuário e senha.
      </span>
    `;

    return;
  }

  localStorage.setItem("labcalc_logado", "true");

  window.location.href = "dashboard.html";
}

/* =========================
   VERIFICA LOGIN
========================= */

if (
  window.location.pathname.includes("dashboard.html")
) {

  const logado = localStorage.getItem("labcalc_logado");

  if (logado !== "true") {
    window.location.href = "index.html";
  }
}

/* =========================
   LOGOUT
========================= */

function logout() {

  localStorage.removeItem("labcalc_logado");

  window.location.href = "index.html";
}

/* =========================
   MENU RESPONSIVO
========================= */

const menuToggle = document.getElementById("menuToggle");
const sidebar = document.getElementById("sidebar");

menuToggle.addEventListener("click", () => {
  sidebar.classList.toggle("open");
});

/* =========================
   NAVEGAÇÃO ENTRE TELAS
========================= */

const menuItems = document.querySelectorAll(".menu-item");
const calculadoras = document.querySelectorAll(".calculadora");

menuItems.forEach(item => {

  item.addEventListener("click", () => {

    menuItems.forEach(btn => {
      btn.classList.remove("active");
    });

    calculadoras.forEach(calc => {
      calc.classList.remove("active");
    });

    item.classList.add("active");

    const alvo = item.getAttribute("data-target");

    document.getElementById(alvo).classList.add("active");

    if (window.innerWidth <= 768) {
      sidebar.classList.remove("open");
    }

  });

});

/* =========================
   HBA1C
========================= */

async function calcularHba1c() {

  const hba1c = document.getElementById("hba1c_percent").value;
  const ifcc = document.getElementById("ifcc_mmol_mol").value;

  if (hba1c && ifcc) {

    document.getElementById("resultado_hba1c").innerHTML = `
      <span class="erro">
        Digite apenas um dos campos.
      </span>
    `;

    return;
  }

  if (!hba1c && !ifcc) {

    document.getElementById("resultado_hba1c").innerHTML = `
      <span class="erro">
        Preencha um dos campos.
      </span>
    `;

    return;
  }

  let url = `${API_URL}/hba1c?`;

  if (hba1c) {
    url += `hba1c_percent=${encodeURIComponent(hba1c)}`;
  }

  if (ifcc) {
    url += `ifcc_mmol_mol=${encodeURIComponent(ifcc)}`;
  }

  try {

    const response = await fetch(url);
    const data = await response.json();

    if (!response.ok) {
      throw new Error(data.detail);
    }

    document.getElementById("resultado_hba1c").innerHTML = `
      <strong>HbA1c:</strong> ${data.hba1c_percent}%<br>
      <strong>IFCC:</strong> ${data.ifcc_mmol_mol} mmol/mol<br>
      <strong>Glicemia Média:</strong> ${data.glicemia_media_estimada_mgdl} mg/dL
    `;

  } catch (error) {

    document.getElementById("resultado_hba1c").innerHTML = `
      <span class="erro">${error.message}</span>
    `;
  }
}

/* =========================
   PROTEINÚRIA
========================= */

async function calcularProteinuria() {

  const volume = document.getElementById("volume_ml").value;
  const proteina = document.getElementById("proteina_mgdl_24h").value;

  const url = `${API_URL}/proteinuria24h?volume_ml=${encodeURIComponent(volume)}&proteina_mgdl=${encodeURIComponent(proteina)}`;

  try {

    const response = await fetch(url);
    const data = await response.json();

    if (!response.ok) {
      throw new Error(data.detail);
    }

    document.getElementById("resultado_proteinuria").innerHTML = `
      <strong>Proteinúria 24h:</strong><br>
      ${data.proteinuria_24h_mg} mg/24h
    `;

  } catch (error) {

    document.getElementById("resultado_proteinuria").innerHTML = `
      <span class="erro">${error.message}</span>
    `;
  }
}

/* =========================
   RPC
========================= */

async function calcularRPC() {

  const proteina = document.getElementById("proteina_rpc").value;
  const creatinina = document.getElementById("creatinina_rpc").value;

  const url = `${API_URL}/rpc?proteina_mgdl=${encodeURIComponent(proteina)}&creatinina_mgdl=${encodeURIComponent(creatinina)}`;

  try {

    const response = await fetch(url);
    const data = await response.json();

    if (!response.ok) {
      throw new Error(data.detail);
    }

    document.getElementById("resultado_rpc").innerHTML = `
      <strong>Relação Proteína/Creatinina:</strong><br>
      ${data.relacao_proteina_creatinina}
    `;

  } catch (error) {

    document.getElementById("resultado_rpc").innerHTML = `
      <span class="erro">${error.message}</span>
    `;
  }
}