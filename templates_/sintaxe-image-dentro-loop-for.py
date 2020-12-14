

def exemplo():
    """"""
    # No exemplo abaixo, temos um loop for interagindo com um template (sintaxe Python & Django no template)
    # 1. <img class="img-fluid" src="{{ field.avatar.Thumb.url }}" alt="">
    # 2. src="{{ var_interna_loop.campo.campo_chave_do_parâmetro_variations.url }}"

    """
    <div class="row">
      {% for field in staff %}
      <div class="col-lg-6 col-md-12 col-xs-12">
        <div class="team-item wow fadeInRight" data-wow-delay="0.2s">
          <div class="team-img">
            <img class="img-fluid" src="{{ field.avatar.Thumb.url }}" alt="{{ field.name }}">                                     
          </div>
          <div class="contetn">
            <div class="info-text">
              <h3><a href="#">{{ field.name }}</a></h3>
              <p>{{ field.job_title }}</p>
            </div>
            <p>{{ field.bio }}</p>
            <ul class="social-icons">
              <li><a href="{{ field.facebook }}"><i class="lni-facebook-filled" aria-hidden="true"></i></a></li>
              <li><a href="{{ field.twitter }}"><i class="lni-twitter-filled" aria-hidden="true"></i></a></li>
              <li><a href="{{ field.instagram }}"><i class="lni-instagram-filled" aria-hidden="true"></i></a></li>
            </ul>
          </div>
        </div>
      </div>
      {% endfor %}
    </div>
    """
