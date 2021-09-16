import bs4
from lxml import etree
import pandas as pd


def Ler_Xml2(arquivo):
    with open(arquivo, encoding='utf-8') as a:
        leitura = bs4.BeautifulSoup(a, 'lxml')

        info_complementar = leitura.find('infadic')
        nota = leitura.find('ide')
        emitente = leitura.find('emit')
        destinatario = leitura.find('dest')
        chave = leitura.find('chnfe')
        produtos = leitura.find_all('det')

        tabela = pd.DataFrame(columns = [
            'Natu.Oper',
            'Modelo',
            'Serie',
            'Num NF',
            'Emissao',
            'Tipo Oper',
            'Destino',
            'Tipo Emissao',
            'Finalidade',
            'Cons. Final',
            'Presença',
            'NF Ref.',
            'CNPJ Emit.',
            'Emitente',
            'IE Emit.',
            'UF Emit.',
            'IE Sub. Trib.',
            'Destinatário',
            'CNPJ Dest.',
            'IE Dest.',
            'UF Dest.',
            'Indicador IE',
            'SUFRAMA',
            'EAN',
            'EANtrib',
            'Codigo',
            'Produto',
            'NCM',
            'Ex.',
            'CEST',
            'CFOP',
            'UND',
            'QTD',
            'Preco',
            'Valor',
            'Vlr Frete',
            'Vlr Seguro',
            'Vlr Desconto',
            'Vlr Outros',
            'Origem',
            'CST',
            'Mod.BC',
            'Reduc.BC',
            'Base de Calculo',
            'Alíquota',
            'ICMS s/reduc.',
            'Perc. Diferm.',
            'ICMS Diferido',
            'ICMS',
            'Mod.BCST',
            'MVA',
            'Red.BCST',
            'BCR-ST',
            'Aliq.ST',
            'ICMS-ST',
            'BC da ST ant.',
            'ST anterior',
            'Ali. IPI',
            'Vlr IPI',
            'CST PC',
            'BC PIS',
            'Qtd. BC PIS',
            'Aliq. PIS',
            'PIS qtd.',
            'Vlr PIS',
            'Aliq. COFINS',
            'Vlr. COFINS',
            'Chave',
            'Inf. Compl.',
            'Inf. Fisco'
            ])

        #try:

        indice = 0
        for el in produtos:
            tabela.loc[indice] = [
                nota.find('natop').text,
                nota.find('mod').text,
                nota.find('serie').text,
                nota.find('nnf').text,
                nota.find('dhemi').text,
                gettext(nota.find('tpnf')),
                gettext(nota.find('iddest')),
                gettext(nota.find('tpemis')),
                gettext(nota.find('finnfe')),
                gettext(nota.find('indfinal')),
                gettext(nota.find('indpres')),
                gettext(nota.find('refnfe')),
                getfilho(emitente,'cnpj'),
                getfilho(emitente,'xnome'),
                getfilho(emitente,'ie'),
                gettext(emitente.find('uf')),
                gettext(emitente.find('iest')),
                getfilho(destinatario,'xnome'),
                getfilho(destinatario,'cnpj'),
                getfilho(destinatario,'ie'),
                getfilho(destinatario,'uf'),
                getfilho(destinatario,'indiedest'),
                getfilho(destinatario,'isuf'),
                gettext(el.find('cean')),
                gettext(el.find('ceantrib')),
                gettext(el.find('cprod')),
                gettext(el.find('xprod')),
                gettext(el.find('ncm')),
                gettext(el.find('extipi')),
                gettext(el.find('cest')),
                gettext(el.find('cfop')),
                gettext(el.find('ucom')),
                gettext(el.find('qcom')),
                gettext(el.find('vuncom')),
                gettext(el.find('vprod')),
                gettext(el.find('vfrete')),
                gettext(el.find('vseg')),
                gettext(el.find('vdesc')),
                gettext(el.find('voutro')),
                gettext(el.find('orig')),
                get_simplesnacional(el.find('icms'),'cst','csosn'),
                gettext(el.find('modbc')),
                gettext(el.find('predbc')),
                gettext(el.find('vbc')),
                get_simplesnacional(el.find('icms'),'picms','pcredsn'),
                gettext(el.find('vicmsop')),
                gettext(el.find('pdif')),
                gettext(el.find('vicmsdif')),
                get_simplesnacional(el.find('icms'),'vicms','vcredicmssn'),
                gettext(el.find('modbcst')),           
                gettext(el.find('pmvast')),
                gettext(el.find('predbcst')),
                gettext(el.find('vbcst')),
                gettext(el.find('picmsst')),
                gettext(el.find('vicmsst')),
                gettext(el.find('vbcstrert')),
                gettext(el.find('vicmsstret')),
                getfilho(el.find('ipi'),'pipi'),
                getfilho(el.find('ipi'),'vipi'),
                getfilho(el.find('pis'),'cst'),
                getfilho(el.find('pis'),'vbc'),
                getfilho(el.find('pis'),'qbcprod'),
                getfilho(el.find('pis'),'ppis'),
                getfilho(el.find('pis'),'valiqprod'),
                getfilho(el.find('pis'),'vpis'),
                getfilho(el.find('cofins'),'pcofins'),
                getfilho(el.find('cofins'),'vcofins'),
                chave.text,
                getfilho(info_complementar,'infcpl'),
                getfilho(info_complementar,'infadfisco')
                ]
            indice +=1

            
            

    return tabela

def gettext(elemento):
    if elemento is None:
        return ''
    else:
        return elemento.text

def getfilho(elemento,texto):
    if elemento is None:
        return ''
    elif elemento.find(texto) is None:
        return ''
    else:
        return elemento.find(texto).text

def get_simplesnacional(elemento,normal,simples):
    if elemento.find(normal) != None:
        return elemento.find(normal).text

    elif elemento.find(simples) != None:
        return elemento.find(simples).text

    elif elemento.find(normal) is None:
        return ''
    else:
        return ''