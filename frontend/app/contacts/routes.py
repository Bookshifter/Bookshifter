from flask import render_template
from app.contacts import bp
from flask import current_app


@bp.route('/contacts/<asn>/<ix>')
def contacts(asn,ix):
    cadastro_url = current_app.config.get('CADASTRO_API_URL')
    all_asns_data, ix_atual, ix_atual_code = api_cadastro.get_asns_and_ix(cadastro_url, None, None)
    return render_template('/contacts/contacts.html',
                           all_asns_data=all_asns_data,
                           ix_atual=ix_atual,
                           asn_route=asn,
                           ix_route=ix,
                           cadastro_url=cadastro_url,
                           )

@bp.route('/contacts')
def contacts_mock():
    cadastro_url = current_app.config.get('CADASTRO_API_URL')
    all_asns_data, ix_atual, ix_atual_code = api_cadastro.get_asns_and_ix(cadastro_url, None, None)
    return render_template('/contacts/contacts-mock.html',
                           cadastro_url=cadastro_url,
                           all_asns_data=all_asns_data,
                           ix_atual=ix_atual,
                           )