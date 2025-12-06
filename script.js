/* === DADOS DO JOGO === */
const temas = {
    capitais: {
        1: { palavras: ["recife","joaopessoa","aracaju","maceio","natal","teresina","saoluis","fortaleza","salvador"], dica: "🏙️ Capitais do Nordeste" },
        2: { palavras: ["rioBranco","maceio","macapa","manaus","salvador","fortaleza","brasilia","vitoria","goiania","saoLuis","cuiaba","campoGrande","beloHorizonte","belem","joaoPessoa","curitiba","recife","teresina","rioDeJaneiro","natal","portoAlegre","portoVelho","boaVista","florianopolis","saoPaulo","aracaju","palmas"], dica: "🇧🇷 Capitais do Brasil" },
        3: { palavras: ["londres","paris","roma","madrid","lisboa","berlim","mexico","buenosAires","santiago","milao","veneza","havana","dubai","lima","moscou","pequim","toquio","seul","washington","caracas","cairo","singapura"], dica: "🌍 Capitais do Mundo" }
    },
    animais: {
        1: { palavras: ["gato","cachorro","coelho","peixe","tartaruga","pato","vaca","porco","cavalo","galinha","ovelha"], dica: "🐾 Animais comuns" },
        2: { palavras: ["leao","tigre","elefante","macaco","zebra","girafa","hipopotamo","rinoceronte","urso","crocodilo","panda","lobo","raposa","camelo","golfinho","tartaruga","onca","gorila","jacare","pinguim"], dica: "🦓 Animais selvagens" },
        3: { palavras: ["ornitorrinco","tamandua","bichoPreguica","camelo","lemure","suricato","canguru","avestruz","pavao","barracuda","camaleao","iguana","tucano","flamingo","ariranha","jabuti","golfinhoRosa","capivara","tamanduabandeira","pantera","hiena"], dica: "🐉 Animais exóticos" }
    },
    frutas: {
        1: { palavras: ["abacate","uva","banana","laranja","morango","abacaxi","manga","pera","caju","melancia","limao","melao","maca"], dica: "🍌 Frutas comuns" },
        2: { palavras: ["abacate","cupuacu","pitanga","buriti","coco","caju","melancia","kiwi","ameixa","goiaba","maracuja","pessego","cereja","graviola","figo","acerola","jabuticaba"], dica: "🇧🇷 Frutas variadas" },
        3: { palavras: ["abacate","umbu","pequi","acai","figo","cacau","jabuticaba","pitanga","tamarindo","roma","carambola","cupuacu","jaca","pitaya","marolo","mirtilo","cacau","seriguela","pitomba"], dica: "🥭 Frutas exóticos" }
    }
};

/* === ESTADO DO JOGO === */
let palavraSecreta = "";
let letrasUsadas = [];
let chances = 7;

/* === ELEMENTOS === */
const menu = document.getElementById("menu");
const jogo = document.getElementById("jogo");
const palavraDiv = document.getElementById("palavra");
const chancesSpan = document.getElementById("chances");
const usadasSpan = document.getElementById("usadas");
const mensagem = document.getElementById("mensagem");
const letraInput = document.getElementById("letra");
const videoModal = document.getElementById("video-modal");
const playerVideo = document.getElementById("player-video");
const btnFecharVideo = document.getElementById("fechar-video");
const btnIniciar = document.getElementById("iniciar");
const btnTentar = document.getElementById("tentar");
const btnReiniciar = document.getElementById("reiniciar");
const selectTema = document.getElementById("tema");
const selectNivel = document.getElementById("nivel");

/* === EVENTOS === */
if (btnIniciar) btnIniciar.addEventListener("click", iniciarJogo);
if (btnTentar) btnTentar.addEventListener("click", tentarLetra);
if (btnReiniciar) btnReiniciar.addEventListener("click", reiniciarJogo);

if (btnFecharVideo) {
    btnFecharVideo.addEventListener("click", () => {
        fecharModalVitoria();
        resetGameState();
        menu.classList.remove("hidden");
        jogo.classList.add("hidden");
    });
}

if (letraInput) letraInput.addEventListener("keypress", e => {
    if (e.key === "Enter") tentarLetra();
});

if (selectTema) selectTema.addEventListener("change", atualizarDica);
if (selectNivel) selectNivel.addEventListener("change", atualizarDica);

/* === FUNÇÕES DO JOGO === */
function atualizarDica() {
    if (!selectTema || !selectNivel) return;
    const tema = selectTema.value;
    const nivel = selectNivel.value;
    const dicaTexto = (tema && nivel) ? temas[tema][nivel].dica : "💡 Escolha tema e nível...";

    const dicaMenu = document.getElementById("dica-menu");
    const dicaJogo = document.getElementById("dica-jogo");

    if (dicaMenu) dicaMenu.textContent = dicaTexto;
    if (dicaJogo) dicaJogo.textContent = dicaTexto;
}

function iniciarJogo() {
    if (!selectTema || !selectNivel) return;
    const tema = selectTema.value;
    const nivel = selectNivel.value;
    if (!tema || !nivel) return alert("⚠️ Escolha tema e nível!");

    const lista = temas[tema][nivel].palavras;
    palavraSecreta = lista[Math.floor(Math.random() * lista.length)].toLowerCase();
    letrasUsadas = [];
    chances = 7;

    menu.classList.add("hidden");
    jogo.classList.remove("hidden");
    atualizarTela();
    atualizarDica();
}

function atualizarTela() {
    if (!palavraDiv) return;
    palavraDiv.textContent = palavraSecreta
        .split("")
        .map(l => (letrasUsadas.includes(l) ? l : "_"))
        .join(" ");
    if (chancesSpan) chancesSpan.textContent = chances;
    if (usadasSpan) usadasSpan.textContent = letrasUsadas.join(", ");
}

function tentarLetra() {
    if (!letraInput) return;
    const letra = letraInput.value.toLowerCase().trim();
    letraInput.value = "";
    letraInput.focus();

    if (!letra || letra.length !== 1) return mostrarMensagem("⚠️ Digite uma letra válida!", "#ffeb3b");
    if (letrasUsadas.includes(letra)) return mostrarMensagem("⚠️ Você já tentou essa letra!", "#ffeb3b");

    letrasUsadas.push(letra);
    if (palavraSecreta.includes(letra)) mostrarMensagem("✅ Acertou!", "#4caf50");
    else { chances--; mostrarMensagem("❌ Errou!", "#ffeb3b"); }

    atualizarTela();
    verificarFimDeJogo();
}

function mostrarMensagem(texto, cor) {
    if (!mensagem) return;
    mensagem.textContent = texto;
    mensagem.style.color = cor;
    setTimeout(() => { if (mensagem) mensagem.textContent = ""; }, 2000);
}

function verificarFimDeJogo() {
    if (!palavraSecreta) return;
    const venceu = palavraSecreta.split("").every(l => letrasUsadas.includes(l));

    if (venceu) {
        // Exibe mensagem de vitória por 3 segundos
        mostrarMensagem(`🎉 A palavra é "${palavraSecreta}" 🎉`, "#ffeb3b");
        if (letraInput) letraInput.disabled = true;
        if (btnTentar) btnTentar.disabled = true;

        setTimeout(() => {
            exibirVideoVitoria();
        }, 3000);

        return;
    }
    
    if (chances <= 0) {
        if (letraInput) letraInput.disabled = true;
        if (btnTentar) btnTentar.disabled = true;

        // Mostra mensagem de derrota
        mostrarMensagem(`😢 Poxa! A palavra era "${palavraSecreta}".`, "#ffeb3b");

        // Esconde a tela do jogo após 3 segundos e reinicia
        setTimeout(() => {
            reiniciarJogo();
        }, 3000);
    }
}

/* === VÍDEO DE VITÓRIA === */
function exibirVideoVitoria() {
    if (!videoModal || !playerVideo) return;
    videoModal.classList.remove("hidden");
    try { playerVideo.currentTime = 0; playerVideo.play(); } catch(e){}
}

function fecharModalVitoria() {
    if (!videoModal || !playerVideo) return;
    playerVideo.pause();
    playerVideo.currentTime = 0;
    videoModal.classList.add("hidden");
}

/* === RESET / REINICIAR === */
function resetGameState() {
    palavraSecreta = "";
    letrasUsadas = [];
    chances = 7;
    if (letraInput) { letraInput.disabled = false; letraInput.value = ""; }
    if (btnTentar) btnTentar.disabled = false;
    if (usadasSpan) usadasSpan.textContent = "";
    if (chancesSpan) chancesSpan.textContent = chances;

    const dicaMenu = document.getElementById("dica-menu");
    const dicaJogo = document.getElementById("dica-jogo");

    if (dicaMenu) dicaMenu.textContent = "💡 Dica aparecerá aqui...";
    if (dicaJogo) dicaJogo.textContent = "💡 Dica aparecerá aqui...";

    atualizarTela();
}

function reiniciarJogo() {
    resetGameState();
    jogo.classList.add("hidden");
    menu.classList.remove("hidden");
}
