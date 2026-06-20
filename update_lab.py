import os

lab_html = r"""  <!-- ============================
       HERO SECTION - LAB
       ============================ -->
  <header class="hero" id="hero">
    <div class="container hero-inner">
      <div class="hero-content">
        <span class="eyebrow" data-i18n="lab_hero_eyebrow">Jiu-Jitsu Technical Study Sessions</span>
        <h1 class="heading-display hero-title" data-i18n="lab_hero_title">Technique<br>conquers all</h1>
        <p class="text-body text-light hero-subtitle" data-i18n="lab_hero_subtitle">Sessões de drill, análise técnica e refinamento do BJJ.</p>

        <div class="hero-cta-group">
          <a href="https://wa.me/5583999619497" target="_blank" rel="noopener" class="btn btn-primary" id="heroCta">
            <span data-i18n="lab_cta_primary">Entrar no grupo</span>
          </a>
          <a href="#concept" class="btn btn-secondary" data-i18n="lab_cta_secondary">Ver formato</a>
        </div>
      </div>
    </div>
    
    <div class="hero-scroll-indicator" aria-hidden="true">
      <span class="scroll-text" data-i18n="hero_scroll">Scroll</span>
      <div class="scroll-line"></div>
    </div>
  </header>

  <!-- ============================
       CONCEPT SECTION
       ============================ -->
  <section class="section" id="concept">
    <div class="container">
      <div class="section-header text-center fade-up">
        <span class="eyebrow" data-i18n="lab_concept_eyebrow">O Conceito</span>
        <h2 class="heading-display heading-lg" data-i18n="lab_concept_title">Estudo e Refinamento</h2>
        <p class="text-body text-light" style="max-width: 600px; margin: 0 auto;" data-i18n="lab_concept_desc">Treinos focados em drill, estudo técnico e refinamento de movimento no Jiu-Jitsu. O objetivo não é sparring livre, mas estudo, repetição consciente e evolução técnica.</p>
      </div>
    </div>
  </section>

  <!-- ============================
       HOW IT WORKS
       ============================ -->
  <section class="section bg-muted" id="how-it-works">
    <div class="container">
      <div class="grid" style="grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: var(--space-lg);">
        <div class="card fade-up">
          <h3 class="heading-display heading-md" data-i18n="lab_hw_1_title">1. Luta Referência</h3>
          <p class="text-body text-muted" data-i18n="lab_hw_1_desc">Cada encontro parte da análise de uma luta referência para entender o timing, a alavanca e a aplicação em alto nível.</p>
        </div>
        <div class="card fade-up" style="transition-delay: 100ms;">
          <h3 class="heading-display heading-md" data-i18n="lab_hw_2_title">2. Drill Específico</h3>
          <p class="text-body text-muted" data-i18n="lab_hw_2_desc">Repetição isolada do movimento. Construção da memória muscular e precisão biomecânica sem a resistência de um combate real.</p>
        </div>
        <div class="card fade-up" style="transition-delay: 200ms;">
          <h3 class="heading-display heading-md" data-i18n="lab_hw_3_title">3. Foco Técnico</h3>
          <p class="text-body text-muted" data-i18n="lab_hw_3_desc">Aplicação com resistência progressiva. Resolução de problemas nas posições e detalhamento refinado das mecânicas ocultas.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- ============================
       FREE DRILL
       ============================ -->
  <section class="section" id="free-drill">
    <div class="container">
      <div class="card" style="display: flex; flex-direction: column; align-items: center; text-align: center; max-width: 800px; margin: 0 auto;">
        <span class="eyebrow" data-i18n="lab_drill_eyebrow">Prática Autônoma</span>
        <h2 class="heading-display heading-lg" data-i18n="lab_drill_title">Drill Livre</h2>
        <p class="text-body text-muted" data-i18n="lab_drill_desc">Tempo dedicado para você e seu parceiro trabalharem posições específicas, tirarem dúvidas e polirem o jogo com supervisão técnica, sem pressão de rendimento.</p>
      </div>
    </div>
  </section>

  <!-- ============================
       AUDIENCE
       ============================ -->
  <section class="section bg-muted" id="audience">
    <div class="container">
      <div class="grid" style="grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: var(--space-lg);">
        <div class="card fade-up" style="border-left: 4px solid var(--color-secondary);">
          <h3 class="heading-display heading-md" data-i18n="lab_for_title">Para quem é</h3>
          <ul class="text-body text-muted" style="list-style-type: disc; margin-left: var(--space-sm);">
            <li data-i18n="lab_for_1">Quem quer entender a biomecânica das posições.</li>
            <li data-i18n="lab_for_2">Atletas buscando refinar movimentos antes da exaustão.</li>
            <li data-i18n="lab_for_3">Praticantes que valorizam a repetição inteligente.</li>
          </ul>
        </div>
        <div class="card fade-up" style="border-left: 4px solid #cc0000; transition-delay: 100ms;">
          <h3 class="heading-display heading-md" data-i18n="lab_not_title">O que não é</h3>
          <ul class="text-body text-muted" style="list-style-type: disc; margin-left: var(--space-sm);">
            <li data-i18n="lab_not_1">Não é dia de 'porradaria' ou sparring de alta intensidade.</li>
            <li data-i18n="lab_not_2">Não é para quem busca apenas suar sem pensar.</li>
            <li data-i18n="lab_not_3">Não é uma aula convencional com dezenas de posições.</li>
          </ul>
        </div>
      </div>
    </div>
  </section>

  <!-- ============================
       LOCATIONS & STRUCTURE
       ============================ -->
  <section class="section" id="locations">
    <div class="container">
      <div class="section-header text-center fade-up">
        <h2 class="heading-display heading-lg" data-i18n="lab_locations_title">Locais e Estrutura</h2>
      </div>
      <div class="grid" style="grid-template-columns: 1fr; max-width: 600px; margin: 0 auto;">
        <div class="card fade-up text-center">
          <h3 class="heading-display heading-md">João Pessoa, PB</h3>
          <p class="text-body text-muted" data-i18n="lab_locations_desc">A definir. O formato será itinerante ou em local fixo selecionado para garantir a melhor experiência de aprendizado.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- ============================
       FINAL CTA
       ============================ -->
  <section class="section bg-muted" id="cta" style="border-top: 1px solid var(--color-border); border-bottom: 1px solid var(--color-border);">
    <div class="container" style="display: flex; flex-direction: column; align-items: center; text-align: center;">
      <span class="eyebrow" data-i18n="lab_cta_final_eyebrow">Faça parte</span>
      <h2 class="heading-display heading-xl" data-i18n="lab_cta_final_title">Evolução<br>Consciente</h2>
      <p class="text-body text-light" style="max-width: 500px; margin-bottom: var(--space-lg);" data-i18n="lab_cta_final_desc">Junte-se ao grupo focado no refinamento técnico e leve seu Jiu-Jitsu para o próximo nível.</p>

      <a href="https://wa.me/5583999619497" target="_blank" rel="noopener" class="btn btn-whatsapp" id="finalCta">
        <svg class="whatsapp-icon" viewBox="0 0 24 24" aria-hidden="true"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg>
        <span data-i18n="lab_cta_btn">Falar no WhatsApp</span>
      </a>
    </div>
  </section>
\n"""

file_path = "c:/Users/vlant/awaken-bjj/lab.html"
with open(file_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

# Find the start of hero and the start of footer
start_idx = -1
end_idx = -1

for i, line in enumerate(lines):
    if '<header class="hero"' in line:
        start_idx = i
    if '<footer class="footer"' in line:
        end_idx = i
        break

if start_idx != -1 and end_idx != -1:
    new_lines = lines[:start_idx] + [lab_html] + lines[end_idx:]
    with open(file_path, "w", encoding="utf-8") as f:
        f.writelines(new_lines)
    print("Replaced content successfully.")
else:
    print(f"Indices not found. start: {start_idx}, end: {end_idx}")
