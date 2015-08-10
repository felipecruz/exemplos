from collections import namedtuple

ExecucaoFianceira = namedtuple('ExecucaoFianceira',
                               ['IdExecucaoFinanceira',
                               'IdEmpreendimento',
                               'IdInstituicaoContratado',
                               'IdPessoaFisicaContratado',
                               'IdLicitacao',
                               'ValContrato',
                               'ValTotal',
                               'DatAssinatura',
                               'DatInicioVigencia',
                               'DatFinalVigencia'])

execucao = ExecucaoFianceira(
    '1',
    '2',
    '132',
    '-1',
    '76',
    '696648486.09',
    '0',
    '19/03/2010',
    '23/03/2010',
    '05/10/2013'
)

print(execucao.ValContrato)
print(execucao)
