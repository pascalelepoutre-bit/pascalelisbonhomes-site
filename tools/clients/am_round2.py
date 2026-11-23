P='https://ireland.apollo.olxcdn.com/v1/files/eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.'
S='/image;s=1280x1024;q=80'
CS='https://media.casasapo.pt/Z1440x1080/'
UC=lambda i:'https://uploadcare.engelvoelkers.com/'+i+'/-/resize/1400x/'
IDL='https://img4.idealista.pt/blur/WEB_DETAIL/0/id.pro.pt.image.master/'
iv=lambda L:[P+x+S for x in L]
cs=lambda L:[CS+x for x in L]
J='eyJ3IjpbeyJmbiI6IjY5bmxwYTdlY3FtNzEtQVBUIiwicyI6IjE2IiwiYSI6IjAiLCJwIjoiMTAsLTEwIn1dfQ'
HOUSES=[
 dict(id='casimiro',name='Rua Joaquim Casimiro, Lapa',price='695 000 €',state='Pronta a habitar',ready=True,
  line='T3 · 110 m² · 1.º andar · pátio privativo',
  photos=iv(['eyJmbiI6IjM1OXNvcnhudjN3dTItRUNPU1lTVEVNIiwidyI6W3siZm4iOiI2OW5scGE3ZWNxbTcxLUFQVCIsInMiOiIxNiIsImEiOiIwIiwicCI6IjEwLC0xMCJ9XX0.rHevQHoH18QgxgkazWi0gQy-xg12zJkeEIxW3kS2VIU','eyJmbiI6Imtyc2tibjkwYWxlMi1FQ09TWVNURU0iLCJ3IjpbeyJmbiI6IjY5bmxwYTdlY3FtNzEtQVBUIiwicyI6IjE2IiwiYSI6IjAiLCJwIjoiMTAsLTEwIn1dfQ.ImgBhI4VJdlmynoXPIZCnQTa8sBN0j_8-gpiq9JVNbs','eyJmbiI6ImxuYmU1MDZqcGtnbDItRUNPU1lTVEVNIiwidyI6W3siZm4iOiI2OW5scGE3ZWNxbTcxLUFQVCIsInMiOiIxNiIsImEiOiIwIiwicCI6IjEwLC0xMCJ9XX0.nTobWvQAyyxm81Qla_i6MDRlNkZROgVgVU7hSWZQegM','eyJmbiI6InY3MHJkeG1qa2ViNC1FQ09TWVNURU0iLCJ3IjpbeyJmbiI6IjY5bmxwYTdlY3FtNzEtQVBUIiwicyI6IjE2IiwiYSI6IjAiLCJwIjoiMTAsLTEwIn1dfQ.VDzsg8tjsRvjfH7MEfSjuJTzkjU6OWdJ0UA5kGwy4zo','eyJmbiI6InZudDRoaDVqYTE3dDItRUNPU1lTVEVNIiwidyI6W3siZm4iOiI2OW5scGE3ZWNxbTcxLUFQVCIsInMiOiIxNiIsImEiOiIwIiwicCI6IjEwLC0xMCJ9XX0.KylkB1-hav3eu3CH5vTBlVHOmZdUJrIX4SmXt9pkPFI']),
  link='https://www.imovirtual.com/pt/anuncio/t3-elegante-e-repleto-de-charme-na-lapa-ID1i8hT',
  why=['Sala e zona de refeições em open space, exatamente o que me descreveram.','Tetos trabalhados, muita luz e carácter em todas as divisões.','Um pequeno pátio privativo nas traseiras, raro nesta zona.'],
  fit=[('ok','Sala grande com cozinha aberta'),('ok','Charme e luz'),('ok','3 quartos'),('mid','695 000 €, à venda desde abril: há margem para negociar')],
  note='Prédio de 1975. Confirmo na visita o pé-direito, o estado das casas de banho e o condomínio.',
  facts=[('Área','110 m²'),('Quartos','3'),('Piso','1.º'),('Exterior','Pátio privativo'),('Construção','1975'),('Energia','Classe C')],
  maps='Rua Joaquim Casimiro, Lisboa'),
 dict(id='bica',name='Travessa do Cabral, Bica',price='490 000 €',state='Para recuperar',ready=False,
  line='T4 · 115 m² · dois pátios interiores',
  photos=iv(['eyJmbiI6ImlpamJ1d2EyM21udzEtRUNPU1lTVEVNIiwidyI6W3siZm4iOiI2OW5scGE3ZWNxbTcxLUFQVCIsInMiOiIxNiIsImEiOiIwIiwicCI6IjEwLC0xMCJ9XX0.3_Wsb_AKM8X-GscfY2FSkAadoyByBjg6OcyWxNphlFc','eyJmbiI6ImV1N2h0ZGdvYXFqMjItRUNPU1lTVEVNIiwidyI6W3siZm4iOiI2OW5scGE3ZWNxbTcxLUFQVCIsInMiOiIxNiIsImEiOiIwIiwicCI6IjEwLC0xMCJ9XX0.-Dpn8GMS5pUb_DhJ6y5tdMGV8Ve5Bmrp4JE2GGEax5A','eyJmbiI6InlwY2I0cmlrOGU5ejEtRUNPU1lTVEVNIiwidyI6W3siZm4iOiI2OW5scGE3ZWNxbTcxLUFQVCIsInMiOiIxNiIsImEiOiIwIiwicCI6IjEwLC0xMCJ9XX0.qy9vLVJ8DAmk675rZusT3c3tVTJmNg6AGHEnWhhz7Zc','eyJmbiI6InBjOW5mY2h1NGdncy1FQ09TWVNURU0iLCJ3IjpbeyJmbiI6IjY5bmxwYTdlY3FtNzEtQVBUIiwicyI6IjE2IiwiYSI6IjAiLCJwIjoiMTAsLTEwIn1dfQ.vh3U5r0XnYXs8Gt-r8Me7Ir9qGF-q9wpsQiEODkJrlo','eyJmbiI6Imh3NTIxNnQzN2Uzay1FQ09TWVNURU0iLCJ3IjpbeyJmbiI6IjY5bmxwYTdlY3FtNzEtQVBUIiwicyI6IjE2IiwiYSI6IjAiLCJwIjoiMTAsLTEwIn1dfQ.aYDQlHZx9qKUDXEiCSlC3aCPovX9vRf5AaBEbfrNlUc']),
  link='https://www.imovirtual.com/pt/anuncio/apartamento-t4-para-recuperar-na-bica-misericor-ID1j8Xj',
  why=['Um verdadeiro projeto para remodelar à vossa medida, num dos bairros mais autênticos de Lisboa.','Quatro quartos e dois pátios interiores: espaço para crescer.','Entre Santos e o Cais do Sodré, a poucos minutos a pé do vosso trabalho.'],
  fit=[('ok','Remodelar ao vosso gosto'),('ok','Espaço para família'),('ok','Perto do rio e do comboio'),('ok','Com obras, bem abaixo dos 800 000 €')],
  note='Precisa de obras completas e tem só uma casa de banho. A Bica pode ser animada à noite: confirmo o ruído da rua.',
  facts=[('Área','115 m²'),('Quartos','4'),('Casas de banho','1'),('Exterior','2 pátios interiores'),('Estado','Para recuperar'),('Energia','Classe C')],
  maps='Travessa do Cabral, Lisboa'),
 dict(id='boahora',name='Calçada da Boa Hora, Alcântara',price='499 000 €',state='Pronta a habitar',ready=True,
  line='T2 · 89 m² · varanda',
  photos=cs(['OAYES/S5/C5462/P31369153/Tphoto/IDc1a7de01-0000-0500-0000-00001accb7d1.jpg','OAYES/S5/C5462/P31369153/Tphoto/IDc1a7de01-0000-0500-0000-00001accb7ca.jpg','OAYES/S5/C5462/P31369153/Tphoto/IDc1a7de01-0000-0500-0000-00001accb7d5.jpg','OAYES/S5/C5462/P31369153/Tphoto/IDc1a7de01-0000-0500-0000-00001accb7d9.jpg','OAYES/S5/C5462/P31369153/Tphoto/IDc1a7de01-0000-0500-0000-00001accb7dd.jpg','OAYES/S5/C5462/P31369153/Tphoto/IDc1a7de01-0000-0500-0000-00001accb7e0.jpg']),
  link='https://casa.sapo.pt/comprar-apartamento-t2-lisboa-alcantara-cc1678a4-d813-11f1-9c13-060000000051.html',
  why=['Traça lisboeta com sancas e soalho, renovada com cuidado.','Cozinha bonita e uma varanda.','Muito abaixo do vosso orçamento, perto de Belém, do rio e do comboio.'],
  fit=[('ok','Charme e luz'),('mid','Cozinha separada da sala'),('mid','2 quartos'),('ok','499 000 €, abaixo do limite do IMT Jovem')],
  note='Só tem dois quartos. Estacionamento possível em avença por 90 € por mês.',
  facts=[('Área','89 m² área bruta privativa'),('Quartos','2'),('Exterior','Varanda'),('Estado','Remodelado')],
  maps='Calçada da Boa Hora, Lisboa'),
 dict(id='esperanca',name='Rua da Esperança, Santos',price='880 000 €',state='Para remodelar',ready=False,
  line='T3+2 · 165 m² · pé-direito de 3,32 m',
  photos=iv(['eyJmbiI6Im91cDg0bjhrdTRzYi1FQ09TWVNURU0iLCJ3IjpbeyJmbiI6IjY5bmxwYTdlY3FtNzEtQVBUIiwicyI6IjE2IiwiYSI6IjAiLCJwIjoiMTAsLTEwIn1dfQ.M1YC7VAG5-XhLMNCbwqqDeXCUAqpBdxAOwo8DD4kbGY','eyJmbiI6ImRwNmh4MHh3Znd6djEtRUNPU1lTVEVNIiwidyI6W3siZm4iOiI2OW5scGE3ZWNxbTcxLUFQVCIsInMiOiIxNiIsImEiOiIwIiwicCI6IjEwLC0xMCJ9XX0.XvexbpHzQNBjSxm6IijKoY3FXpvLQS8qoNOVXxwxQwg','eyJmbiI6IjJldW1vNjhyMWo0MjEtRUNPU1lTVEVNIiwidyI6W3siZm4iOiI2OW5scGE3ZWNxbTcxLUFQVCIsInMiOiIxNiIsImEiOiIwIiwicCI6IjEwLC0xMCJ9XX0.x21aF0LpZI9re484Pv1lC6ie4NEkx-t1KV4vNKyRru8','eyJmbiI6ImllMmJ2MHNsbjV0ay1FQ09TWVNURU0iLCJ3IjpbeyJmbiI6IjY5bmxwYTdlY3FtNzEtQVBUIiwicyI6IjE2IiwiYSI6IjAiLCJwIjoiMTAsLTEwIn1dfQ.S13jlbm1gdF_OheQ-9zOdH81Kw59d9dhNN9j8mjkMo0','eyJmbiI6IjZhejVrMnViNTQ0ODMtRUNPU1lTVEVNIiwidyI6W3siZm4iOiI2OW5scGE3ZWNxbTcxLUFQVCIsInMiOiIxNiIsImEiOiIwIiwicCI6IjEwLC0xMCJ9XX0.QeGwWUAgUYRjQB-0jCPla6aXB1x8j3B0ZMyuUYVO01k']),
  link='https://www.imovirtual.com/pt/anuncio/t3-2-na-estrela-santos-o-velho-centro-de-lisboa-ID1h2UI',
  why=['Prédio antigo com fachada de azulejos, tetos altos de 3,32 m, soalho de tábua corrida e portadas de madeira.','Janelas em três fachadas, com sol ao longo do dia.','Muito espaço: dá para a sala grande que querem e quartos para a família.'],
  fit=[('ok','Grandes volumes e carácter'),('ok','Espaço para família'),('ok','Muita luz'),('mid','Só cabe no orçamento com uma boa negociação')],
  note='Precisa de remodelação. Está à venda desde agosto de 2025, por isso vale a pena perguntar quanto o proprietário aceita.',
  facts=[('Área','165 m²'),('Tipologia','T3+2'),('Pé-direito','3,32 m'),('Exposição','Oeste, sudeste e noroeste'),('Estado','Para remodelar'),('Energia','Classe D')],
  maps='Rua da Esperança, Lisboa'),
 dict(id='marques',name='Calçada Marquês de Abrantes, Santos',price='975 000 €',state='Pronta a habitar',ready=True,
  line='T3 · 165 m² · 2.º andar · prédio pombalino',
  photos=iv(['eyJmbiI6InlxaWxpMDd2dDVkcDEtRUNPU1lTVEVNIiwidyI6W3siZm4iOiI2OW5scGE3ZWNxbTcxLUFQVCIsInMiOiIxNiIsImEiOiIwIiwicCI6IjEwLC0xMCJ9XX0.DCViDs6JxtTfsTX04CGNhflJDEMwaP1oT5Xe7zelZO4','eyJmbiI6IjR3bnd3cTBmNTljZzMtRUNPU1lTVEVNIiwidyI6W3siZm4iOiI2OW5scGE3ZWNxbTcxLUFQVCIsInMiOiIxNiIsImEiOiIwIiwicCI6IjEwLC0xMCJ9XX0.Io4NzRy-R-4lB4dEpMRi3lzfA4QQhb04kVhXVFkzbnM','eyJmbiI6IjY5a2V2N2NsNDEyMDMtRUNPU1lTVEVNIiwidyI6W3siZm4iOiI2OW5scGE3ZWNxbTcxLUFQVCIsInMiOiIxNiIsImEiOiIwIiwicCI6IjEwLC0xMCJ9XX0.ivpRo_sVPwehaxa-pVYF_CNrC1m71Mu10C04aLEoK-o','eyJmbiI6IjJnNzU1dm9vOWlpMjEtRUNPU1lTVEVNIiwidyI6W3siZm4iOiI2OW5scGE3ZWNxbTcxLUFQVCIsInMiOiIxNiIsImEiOiIwIiwicCI6IjEwLC0xMCJ9XX0.NmFK2ezpu30e9Tk0H4yUC4dK0arMtiuu9OxDOhQG1wk','eyJmbiI6ImRsaHdiNGsyZTQyMDEtRUNPU1lTVEVNIiwidyI6W3siZm4iOiI2OW5scGE3ZWNxbTcxLUFQVCIsInMiOiIxNiIsImEiOiIwIiwicCI6IjEwLC0xMCJ9XX0.IC6Rjs7Pjzb4xF-gr0He9qCc57DDsBwcNUNwcWhFqV4']),
  link='https://www.imovirtual.com/pt/anuncio/charmoso-t3-na-calcada-marques-dabrantes-ID1hk7X',
  why=['Totalmente recuperado em 2026, mantendo a traça original: pé-direito alto e tetos de madeira.','Sala espaçosa ligada à cozinha, duas suites.','Grandes volumes e muita personalidade, em Santos.'],
  fit=[('ok','Sala com cozinha integrada'),('ok','Pé-direito alto e carácter'),('ok','3 quartos, 2 suites'),('mid','975 000 €: muito acima, só com uma descida grande')],
  note='Mostro-vos esta casa como referência do que procuram. Está à venda há muito tempo; pergunto o que o proprietário aceitaria.',
  facts=[('Área','165 m²'),('Quartos','3, dois em suite'),('Piso','2.º'),('Estado','Recuperado em 2026'),('Prédio','Pombalino, áreas comuns em obras'),('Energia','Classe E')],
  maps='Calçada do Marquês de Abrantes, Lisboa'),
 dict(id='boavista',name='Rua da Boavista, Santos',price='670 000 €',state='Pronta a habitar',ready=True,
  line='Duplex T3 · 104 m² · 4.º andar · sala a sul',
  photos=iv(['eyJmbiI6Im50eW50ZjhpdzJuNjMtRUNPU1lTVEVNIiwidyI6W3siZm4iOiI2OW5scGE3ZWNxbTcxLUFQVCIsInMiOiIxNiIsImEiOiIwIiwicCI6IjEwLC0xMCJ9XX0.tPwwwlxt0RtKxjVfb7SbUF7R5VjZ7kQTCuLL1aTOV9g','eyJmbiI6ImE3YzU5dWhsamNpay1FQ09TWVNURU0iLCJ3IjpbeyJmbiI6IjY5bmxwYTdlY3FtNzEtQVBUIiwicyI6IjE2IiwiYSI6IjAiLCJwIjoiMTAsLTEwIn1dfQ.rK70yGsfNe6T9ut_HgBjhPee79mw4jC1yefQVFcaMH0','eyJmbiI6IjU5bWhqbDJzeHByajItRUNPU1lTVEVNIiwidyI6W3siZm4iOiI2OW5scGE3ZWNxbTcxLUFQVCIsInMiOiIxNiIsImEiOiIwIiwicCI6IjEwLC0xMCJ9XX0.2_pfW-MrZYslftYltFleuO5m-4y8K8dwwhOPTpKUyBc','eyJmbiI6IjM4bXVmcnZ5OXFxZi1FQ09TWVNURU0iLCJ3IjpbeyJmbiI6IjY5bmxwYTdlY3FtNzEtQVBUIiwicyI6IjE2IiwiYSI6IjAiLCJwIjoiMTAsLTEwIn1dfQ.4LD8MH08Lp7tPs_fYMGvgoUFObROMUYQt9vJxMjGudc','eyJmbiI6IjI4Z25vdTlmd3J0Zi1FQ09TWVNURU0iLCJ3IjpbeyJmbiI6IjY5bmxwYTdlY3FtNzEtQVBUIiwicyI6IjE2IiwiYSI6IjAiLCJwIjoiMTAsLTEwIn1dfQ.HOsu3yKtJ8r4frDF8h91M1pmeK_Bw40TC5LavmIQuvE']),
  link='https://www.imovirtual.com/pt/anuncio/duplex-t3-com-vista-santos-o-velho-lisboa-ID1iBoi',
  why=['Edifício histórico totalmente reabilitado, com a traça original preservada.','Sala e varanda viradas a sul, com muita luz.','Em Santos, perto do Cais do Sodré, onde trabalham.'],
  fit=[('ok','Luz a sul'),('ok','Carácter'),('ok','3 quartos'),('mid','670 000 €, um pouco acima do limite do IMT Jovem')],
  note='Duplex num 4.º andar: confirmo se há elevador e como é a cozinha.',
  facts=[('Área','104 m² no portal, cerca de 147 m² segundo a descrição'),('Tipologia','T3 duplex'),('Piso','4.º'),('Exposição','Sul'),('Energia','Classe C')],
  maps='Rua da Boavista, Lisboa'),
 dict(id='becoolival',name='Rua Joaquim Casimiro / Beco do Olival, Lapa',price='725 000 €',state='Para remodelar',ready=False,
  line='T4+1 · 185 m² área bruta privativa · 3.º andar · vista rio',
  photos=iv(['eyJmbiI6InNzZGE4OW9qZDdiZS1FQ09TWVNURU0iLCJ3IjpbeyJmbiI6IjY5bmxwYTdlY3FtNzEtQVBUIiwicyI6IjE2IiwiYSI6IjAiLCJwIjoiMTAsLTEwIn1dfQ.e-PWQzerrhVSsWD60IJHyRcbD4d8p91teMfzfM7syGA','eyJmbiI6ImU1Nm4xejY2ZWR6ZzItRUNPU1lTVEVNIiwidyI6W3siZm4iOiI2OW5scGE3ZWNxbTcxLUFQVCIsInMiOiIxNiIsImEiOiIwIiwicCI6IjEwLC0xMCJ9XX0.HsEcg0qA-QzDIni_tNO8Xuo3sNwkhITehetug1V4cqs','eyJmbiI6ImE3eWtvYzZhZzgxajEtRUNPU1lTVEVNIiwidyI6W3siZm4iOiI2OW5scGE3ZWNxbTcxLUFQVCIsInMiOiIxNiIsImEiOiIwIiwicCI6IjEwLC0xMCJ9XX0.SVQ-vPeZ_geH4-eyxOxUpHtD_KQvKDrA8q7CjWWkPdk','eyJmbiI6IjRkOXVxNW5kM3lnZjEtRUNPU1lTVEVNIiwidyI6W3siZm4iOiI2OW5scGE3ZWNxbTcxLUFQVCIsInMiOiIxNiIsImEiOiIwIiwicCI6IjEwLC0xMCJ9XX0.8KTAnpD4AaqqYj_NLuE8-MGOw8AZKQQKnuCK66NmR7g','eyJmbiI6InIxdXhhaGd1eWp1NzEtRUNPU1lTVEVNIiwidyI6W3siZm4iOiI2OW5scGE3ZWNxbTcxLUFQVCIsInMiOiIxNiIsImEiOiIwIiwicCI6IjEwLC0xMCJ9XX0.oOGkLmZ1SPQQoB4vV7b05GQynEJJtd_qV223uPyWaYg']),
  link='https://www.imovirtual.com/pt/anuncio/apartamento-t4-para-venda-ID1j4R0',
  why=['Muito espaço: sala de 30 m² com varanda e vista rio, mais sala de jantar e salinha.','Soalho de tábua corrida e quatro quartos, um deles em suite.','Dá para criar a sala grande com cozinha aberta e ainda ter quartos para todos.'],
  fit=[('ok','Espaço para família'),('ok','Vista rio e varanda'),('mid','Cozinha aberta, com obras'),('mid','Com obras, perto dos 800 000 €')],
  note='3.º andar sem elevador, prédio de 1951. Precisa de atualização.',
  facts=[('Área','185 m² área bruta privativa'),('Quartos','4, um em suite'),('Casas de banho','2'),('Piso','3.º, sem elevador'),('Construção','1951'),('Energia','Classe D')],
  maps='Rua Joaquim Casimiro 2, Lisboa'),
 dict(id='algesrio',name='Algés, vista rio',price='660 000 €',state='Para atualizar',ready=False,
  line='T3 · 137 m² · 3.º andar sem elevador',
  photos=cs(['OAYES/S5/C3796/P31370251/Tphoto/ID0bacde01-0000-0500-0000-00001acd2605.jpg','OAYES/S5/C3796/P31370251/Tphoto/ID0bacde01-0000-0500-0000-00001acd2608.jpg','OAYES/S5/C3796/P31370251/Tphoto/ID0bacde01-0000-0500-0000-00001acd260c.jpg','OAYES/S5/C3796/P31370251/Tphoto/ID0bacde01-0000-0500-0000-00001acd2611.jpg','OAYES/S5/C3796/P31370251/Tphoto/ID0bacde01-0000-0500-0000-00001acd2619.jpg','OAYES/S5/C3796/P31370251/Tphoto/ID0bacde01-0000-0500-0000-00001acd2622.jpg']),
  link='https://casa.sapo.pt/comprar-apartamento-t3-oeiras-alges-linda-a-velha-e-cruz-quebrada-dafundo-ad8a4d7f-d821-11f1-b6e5-060000000058.html',
  why=['Vista sobre o Tejo e muita luz.','Duas salas que se podem unir numa sala grande.','Perto da estação de Algés.'],
  fit=[('ok','Vista rio e luz'),('ok','3 quartos, 2 casas de banho'),('mid','Cozinha fechada'),('mid','Rua com muito trânsito')],
  note='Fica numa rua movimentada: confirmo de que lado ficam os quartos.',
  facts=[('Área','137 m² área bruta'),('Quartos','3'),('Casas de banho','2'),('Piso','3.º, sem elevador')],
  maps='Algés, Oeiras'),
 dict(id='madragoa',name='Rua das Madres, Madragoa',price='690 000 €',state='Pronta a habitar',ready=True,
  line='T3 duplex · 130 m² · 3.º andar · vista frontal de rio',
  photos=cs(['OAYES/S5/C1320/P29285166/Tphoto/ID2edbbe01-0000-0500-0000-0000185cb4a5.jpg','OAYES/S5/C1320/P29285166/Tphoto/ID2edbbe01-0000-0500-0000-0000185cb4a8.jpg','OAYES/S5/C1320/P29285166/Tphoto/ID2edbbe01-0000-0500-0000-0000185cb49b.jpg','OAYES/S5/C1320/P29285166/Tphoto/ID2edbbe01-0000-0500-0000-0000185cb4a1.jpg','OAYES/S5/C1320/P29285166/Tphoto/ID2edbbe01-0000-0500-0000-0000185cb4bb.jpg','OAYES/S5/C1320/P29285166/Tphoto/ID2edbbe01-0000-0500-0000-0000185cb4bf.jpg']),
  link='https://casa.sapo.pt/comprar-apartamento-t3-lisboa-estrela-madragoa-(lapa)-0361affd-010b-11f1-b7cf-060000000058.html',
  why=['Vista frontal de rio e muita luz.','Prédio típico com janelas de sacada e azulejos.','Suite, closet e uma sala extra que pode ser quarto.'],
  fit=[('ok','Vista rio e luz'),('ok','3 quartos'),('mid','Cozinha semiaberta, abrir exige obras'),('mid','Só cabe com uma descida de preço')],
  note='3.º andar sem elevador. O piso de cima tem tetos inclinados.',
  facts=[('Área','130 m² área bruta privativa'),('Tipologia','T3 duplex'),('Casas de banho','2'),('Piso','3.º, sem elevador')],
  maps='Rua das Madres, Lisboa'),
 dict(id='saobento',name='São Bento',price='649 000 €',state='Pronta a habitar',ready=True,
  line='T2+1 · 130 m² · remodelado por arquiteto',
  photos=[UC(i) for i in ['20367ee3-b0ec-4b47-a7a4-a9f6fe0f23e9','11642d33-556d-40ea-91fd-bb8e9a93f200','4af56219-669f-4b35-9760-d11efef10cb7','9b1114be-3ea4-4421-8130-4d6ce3035728','acbab6d2-84f1-4399-94b3-986bd603ef63','f40f8b48-f0b8-4496-b32b-1ab75018b0a7']],
  link='https://www.engelvoelkers.com/pt/pt/exposes/680ebb62-ee39-53fc-acb5-b13428f4e26b',
  why=['Prédio pombalino com a gaiola original à vista, remodelado por arquiteto.','Sala de estar e jantar ampla, com muito sol.','Um imóvel Engel & Völkers, por isso marco a visita facilmente.'],
  fit=[('ok','Carácter'),('ok','Muita luz'),('mid','T2+1: o terceiro quarto é pequeno'),('ok','649 000 €, o preço já desceu')],
  note='Confirmo se o +1 serve de quarto e como é a cozinha.',
  facts=[('Área','130 m² área bruta'),('Quartos','2 + 1'),('Casas de banho','2'),('Estado','Remodelado')],
  maps='Rua de São Bento, Lisboa'),
 dict(id='borja',name='Rua do Borja, Prazeres',price='750 000 €',state='Pronta a habitar',ready=True,
  line='T2 · 128 m² área bruta · rés do chão com elevador · jardim e garagem',
  photos=[IDL+'67/e0/88/335277530.jpg'],
  link='https://www.idealista.pt/imovel/35463691/',
  why=['Terraço privativo com jardim, raro em Lisboa.','Garagem com pré-instalação para o carro elétrico.','Prédio de 2012, sem obras.'],
  fit=[('ok','Exterior e garagem'),('mid','2 quartos'),('mid','Construção recente, menos carácter'),('mid','750 000 €')],
  note='Venda direta do proprietário: confirmo primeiro se aceita trabalhar comigo.',
  facts=[('Área','128 m² área bruta'),('Quartos','2'),('Casas de banho','2'),('Piso','Rés do chão, com elevador'),('Garagem','Sim'),('Construção','2012')],
  maps='Rua do Borja 63, Lisboa'),
 dict(id='trinas',name='Rua das Trinas, Lapa',price='600 000 €',state='Pronta a habitar',ready=True,
  line='T2 · 90 m² · 2 casas de banho',
  photos=cs(['OAYES/S5/C9984/P31004269/Tphoto/ID6d16d901-0000-0500-0000-00001a58d5f2.jpg','OAYES/S5/C9984/P31004269/Tphoto/ID6d16d901-0000-0500-0000-00001a58d5f3.jpg','OAYES/S5/C9984/P31004269/Tphoto/ID6d16d901-0000-0500-0000-00001a58d5f4.jpg','OAYES/S5/C9984/P31004269/Tphoto/ID6d16d901-0000-0500-0000-00001a58d5f5.jpg','OAYES/S5/C9984/P31004269/Tphoto/ID6d16d901-0000-0500-0000-00001a58d5f6.jpg','OAYES/S5/C9984/P31004269/Tphoto/ID6d16d901-0000-0500-0000-00001a58d5f7.jpg']),
  link='https://casa.sapo.pt/comprar-apartamento-t2-lisboa-estrela-lapa-63d19934-ad2c-11f1-bc59-060000000052.html',
  why=['Sala de estar e jantar ampla e luminosa.','Cozinha espaçosa e duas casas de banho completas.','O preço desceu de 620 000 € para 600 000 €.'],
  fit=[('ok','Muita luz'),('ok','Sala grande'),('mid','2 quartos'),('ok','600 000 €, abaixo do limite do IMT Jovem')],
  note='Só tem dois quartos.',
  facts=[('Área','90 m²'),('Quartos','2'),('Casas de banho','2'),('Estado','Pronto a habitar')],
  maps='Rua das Trinas, Lisboa'),
]

AREA=dict(casimiro=110,bica=115,boahora=89,esperanca=165,marques=165,boavista=104,becoolival=185,algesrio=137,madragoa=130,saobento=130,borja=128,trinas=90)
for h in HOUSES:
    pr=int(''.join(c for c in h['price'] if c.isdigit()))
    h['ppm']=f"{round(pr/AREA[h['id']]):,}".replace(',',' ')+' €/m²'

GEO=dict(casimiro=(38.70647,-9.166925),bica=(38.70938,-9.14603),boahora=(38.70135,-9.19193),esperanca=(38.70828,-9.1544),marques=(38.70775,-9.15542),boavista=(38.708973,-9.150368),becoolival=(38.705032,-9.167217),algesrio=(38.70054,-9.23334),madragoa=(38.70895,-9.15445),saobento=(38.71546,-9.1543),borja=(38.7108,-9.16911),trinas=(38.71019,-9.1592))
for h in HOUSES: h['geo']=GEO[h['id']]

# 15/11: per house: unique feature, kitchen and floor plan first, with captions
def ivp(x): return P+x+S
def csp(x): return CS+x
NEWPH=dict(
 casimiro=[(ivp('eyJmbiI6IjM1OXNvcnhudjN3dTItRUNPU1lTVEVNIiwidyI6W3siZm4iOiI2OW5scGE3ZWNxbTcxLUFQVCIsInMiOiIxNiIsImEiOiIwIiwicCI6IjEwLC0xMCJ9XX0.rHevQHoH18QgxgkazWi0gQy-xg12zJkeEIxW3kS2VIU'),'Sala'),
  (ivp('eyJmbiI6Iml1bGw5dnVsbGY2OC1FQ09TWVNURU0iLCJ3IjpbeyJmbiI6IjY5bmxwYTdlY3FtNzEtQVBUIiwicyI6IjE2IiwiYSI6IjAiLCJwIjoiMTAsLTEwIn1dfQ.jYmqkT08Kglv_F92ioRLWt-xYaHHzCjw0OgTRb5UCzQ'),'Pátio privativo'),
  (ivp('eyJmbiI6IjE1NThteWVldG9zYTEtRUNPU1lTVEVNIiwidyI6W3siZm4iOiI2OW5scGE3ZWNxbTcxLUFQVCIsInMiOiIxNiIsImEiOiIwIiwicCI6IjEwLC0xMCJ9XX0.Wb5G73QyyirsgclP1yTlYd_2_GvQIP7cg56vXOD1f2s'),'Cozinha'),
  (ivp('eyJmbiI6InRka3p2bDBnMHJiOS1FQ09TWVNURU0iLCJ3IjpbeyJmbiI6IjY5bmxwYTdlY3FtNzEtQVBUIiwicyI6IjE2IiwiYSI6IjAiLCJwIjoiMTAsLTEwIn1dfQ.uUOEZrC7QZ60EhgAuA-x-EhbRF7MwcGMXwSBdAHzwUc'),'Cozinha'),
  (ivp('eyJmbiI6ImxuYmU1MDZqcGtnbDItRUNPU1lTVEVNIiwidyI6W3siZm4iOiI2OW5scGE3ZWNxbTcxLUFQVCIsInMiOiIxNiIsImEiOiIwIiwicCI6IjEwLC0xMCJ9XX0.nTobWvQAyyxm81Qla_i6MDRlNkZROgVgVU7hSWZQegM'),'Sala'),
  (ivp('eyJmbiI6Imd0eHRleHA2ZW04MDItRUNPU1lTVEVNIiwidyI6W3siZm4iOiI2OW5scGE3ZWNxbTcxLUFQVCIsInMiOiIxNiIsImEiOiIwIiwicCI6IjEwLC0xMCJ9XX0._u28_7NC7O5Imkb-PWsfh3SXbGeqSaIJtNtpEfb56qk'),'Quarto'),
  (ivp('eyJmbiI6ImhlaG5qd3h2MGlkZzEtRUNPU1lTVEVNIiwidyI6W3siZm4iOiI2OW5scGE3ZWNxbTcxLUFQVCIsInMiOiIxNiIsImEiOiIwIiwicCI6IjEwLC0xMCJ9XX0.QEoxgqdLWdTTMjpKkL7yBM3HD-jDrqUXbpDV41CaiNQ'),'Planta'),
  (ivp('eyJmbiI6InBsazJmdzMyaHVpZDMtRUNPU1lTVEVNIiwidyI6W3siZm4iOiI2OW5scGE3ZWNxbTcxLUFQVCIsInMiOiIxNiIsImEiOiIwIiwicCI6IjEwLC0xMCJ9XX0.LVpJbgZKWBl3Xgewjr0NqygUUYzxD9-KmjCJV3mtK1I'),'Planta')],
 bica=[(ivp('eyJmbiI6ImV1N2h0ZGdvYXFqMjItRUNPU1lTVEVNIiwidyI6W3siZm4iOiI2OW5scGE3ZWNxbTcxLUFQVCIsInMiOiIxNiIsImEiOiIwIiwicCI6IjEwLC0xMCJ9XX0.-Dpn8GMS5pUb_DhJ6y5tdMGV8Ve5Bmrp4JE2GGEax5A'),'Sala'),
  (ivp('eyJmbiI6Imh3eG5qZTZ6MmV4dC1FQ09TWVNURU0iLCJ3IjpbeyJmbiI6IjY5bmxwYTdlY3FtNzEtQVBUIiwicyI6IjE2IiwiYSI6IjAiLCJwIjoiMTAsLTEwIn1dfQ.zNg0kVUwND2-m7Qp-az4IncvHU_-jVbFlrLmLoYuc4o'),'Pátio interior'),
  (ivp('eyJmbiI6IjVnamdjcnpoMjJwajItRUNPU1lTVEVNIiwidyI6W3siZm4iOiI2OW5scGE3ZWNxbTcxLUFQVCIsInMiOiIxNiIsImEiOiIwIiwicCI6IjEwLC0xMCJ9XX0.pfrG1sdKdjDPGS0OCt4rwFiznmfNo4mzjZXWKE45ask'),'Cozinha'),
  (ivp('eyJmbiI6ImQ5bmZvdWtmMDlwci1FQ09TWVNURU0iLCJ3IjpbeyJmbiI6IjY5bmxwYTdlY3FtNzEtQVBUIiwicyI6IjE2IiwiYSI6IjAiLCJwIjoiMTAsLTEwIn1dfQ.QGm0YOLj6XCAHOJ9hTPJjKnklyYn3ayeaLxpOTWRAgU'),'Exterior'),
  (ivp('eyJmbiI6InBjOW5mY2h1NGdncy1FQ09TWVNURU0iLCJ3IjpbeyJmbiI6IjY5bmxwYTdlY3FtNzEtQVBUIiwicyI6IjE2IiwiYSI6IjAiLCJwIjoiMTAsLTEwIn1dfQ.vh3U5r0XnYXs8Gt-r8Me7Ir9qGF-q9wpsQiEODkJrlo'),'Sala'),
  (ivp('eyJmbiI6Inp1M2lwOWRsY3FkajItRUNPU1lTVEVNIiwidyI6W3siZm4iOiI2OW5scGE3ZWNxbTcxLUFQVCIsInMiOiIxNiIsImEiOiIwIiwicCI6IjEwLC0xMCJ9XX0.ONENpJy8QupR3BlSiA5PcbXYyf2e8POMtYx_wuAUAIk'),'Sala')],
 boavista=[(ivp('eyJmbiI6Im50eW50ZjhpdzJuNjMtRUNPU1lTVEVNIiwidyI6W3siZm4iOiI2OW5scGE3ZWNxbTcxLUFQVCIsInMiOiIxNiIsImEiOiIwIiwicCI6IjEwLC0xMCJ9XX0.tPwwwlxt0RtKxjVfb7SbUF7R5VjZ7kQTCuLL1aTOV9g'),'Sala'),
  (ivp('eyJmbiI6IjN1cTV5ZTh1OXViNi1FQ09TWVNURU0iLCJ3IjpbeyJmbiI6IjY5bmxwYTdlY3FtNzEtQVBUIiwicyI6IjE2IiwiYSI6IjAiLCJwIjoiMTAsLTEwIn1dfQ.KKWSeYWdYGy4Lcs56Jux3Q_2JVdJHNQBqiA74iL5tdg'),'Varanda e vista'),
  (ivp('eyJmbiI6IjdzczNmbWRvNjV4LUVDT1NZU1RFTSIsInciOlt7ImZuIjoiNjlubHBhN2VjcW03MS1BUFQiLCJzIjoiMTYiLCJhIjoiMCIsInAiOiIxMCwtMTAifV19.lxaeGAeJrwW0gZY2_CdJFE-29WeJf9I_c9yHPlDTS4k'),'Cozinha'),
  (ivp('eyJmbiI6InM2Y3k2M2trdmliYi1FQ09TWVNURU0iLCJ3IjpbeyJmbiI6IjY5bmxwYTdlY3FtNzEtQVBUIiwicyI6IjE2IiwiYSI6IjAiLCJwIjoiMTAsLTEwIn1dfQ.S4NQdt7hKoWCGoWE--htfrf8MmvQniz6YKEuGNBnu_w'),'Cozinha'),
  (ivp('eyJmbiI6IjU5bWhqbDJzeHByajItRUNPU1lTVEVNIiwidyI6W3siZm4iOiI2OW5scGE3ZWNxbTcxLUFQVCIsInMiOiIxNiIsImEiOiIwIiwicCI6IjEwLC0xMCJ9XX0.2_pfW-MrZYslftYltFleuO5m-4y8K8dwwhOPTpKUyBc'),'Sala'),
  (ivp('eyJmbiI6IjRveTBwMWhhNnR2bjMtRUNPU1lTVEVNIiwidyI6W3siZm4iOiI2OW5scGE3ZWNxbTcxLUFQVCIsInMiOiIxNiIsImEiOiIwIiwicCI6IjEwLC0xMCJ9XX0.fqyYKPG_pOYKlgf7rt4uGG0yhz6G2PtzJSxxNnEecU0'),'Planta'),
  (ivp('eyJmbiI6Im8xdWU5dHNlYXNoYzEtRUNPU1lTVEVNIiwidyI6W3siZm4iOiI2OW5scGE3ZWNxbTcxLUFQVCIsInMiOiIxNiIsImEiOiIwIiwicCI6IjEwLC0xMCJ9XX0.sVGO4FKIBZuW7MrevkWfy_YnfTN1blMbAC36Q6xg51Y'),'Planta')],
 becoolival=[(ivp('eyJmbiI6InNzZGE4OW9qZDdiZS1FQ09TWVNURU0iLCJ3IjpbeyJmbiI6IjY5bmxwYTdlY3FtNzEtQVBUIiwicyI6IjE2IiwiYSI6IjAiLCJwIjoiMTAsLTEwIn1dfQ.e-PWQzerrhVSsWD60IJHyRcbD4d8p91teMfzfM7syGA'),'Sala'),
  (ivp('eyJmbiI6InIxdXhhaGd1eWp1NzEtRUNPU1lTVEVNIiwidyI6W3siZm4iOiI2OW5scGE3ZWNxbTcxLUFQVCIsInMiOiIxNiIsImEiOiIwIiwicCI6IjEwLC0xMCJ9XX0.oOGkLmZ1SPQQoB4vV7b05GQynEJJtd_qV223uPyWaYg'),'Vista rio'),
  (ivp('eyJmbiI6InB2aWZqcmJuYnBjYzItRUNPU1lTVEVNIiwidyI6W3siZm4iOiI2OW5scGE3ZWNxbTcxLUFQVCIsInMiOiIxNiIsImEiOiIwIiwicCI6IjEwLC0xMCJ9XX0.YZkzh-csaC7E-JMiZEm4PauJFBmEUrqW7LtAaGElNnw'),'Cozinha'),
  (ivp('eyJmbiI6ImsxNDB5d3huY2pscjItRUNPU1lTVEVNIiwidyI6W3siZm4iOiI2OW5scGE3ZWNxbTcxLUFQVCIsInMiOiIxNiIsImEiOiIwIiwicCI6IjEwLC0xMCJ9XX0.8yF29HygUpEL1j5ih7apUXEtSz7GOLIvoFyNziSKZSA'),'Cozinha'),
  (ivp('eyJmbiI6ImtmdzI4cDRsMXMzMy1FQ09TWVNURU0iLCJ3IjpbeyJmbiI6IjY5bmxwYTdlY3FtNzEtQVBUIiwicyI6IjE2IiwiYSI6IjAiLCJwIjoiMTAsLTEwIn1dfQ.n7RhAsbvGkXnlPrj914EK29jjeROT6tbnSVZYjn1Bok'),'Sala de jantar'),
  (ivp('eyJmbiI6ImlnaWJxbTExbGEycDEtRUNPU1lTVEVNIiwidyI6W3siZm4iOiI2OW5scGE3ZWNxbTcxLUFQVCIsInMiOiIxNiIsImEiOiIwIiwicCI6IjEwLC0xMCJ9XX0.ceYahRDKG6C_9xieGXIE8LFxsMO6GsmaMyeTxT3TUz8'),'Planta')],
 boahora=[(csp('OAYES/S5/C5462/P31369153/Tphoto/IDc1a7de01-0000-0500-0000-00001accb80f.jpg'),'Sala'),
  (csp('OAYES/S5/C5462/P31369153/Tphoto/IDc1a7de01-0000-0500-0000-00001accb7ca.jpg'),'Varanda com vista'),
  (csp('OAYES/S5/C5462/P31369153/Tphoto/IDc1a7de01-0000-0500-0000-00001accb7d5.jpg'),'Cozinha'),
  (csp('OAYES/S5/C5462/P31369153/Tphoto/IDc1a7de01-0000-0500-0000-00001accb7d9.jpg'),'Cozinha'),
  (csp('OAYES/S5/C5462/P31369153/Tphoto/IDc1a7de01-0000-0500-0000-00001accb82a.jpg'),'Sala de jantar'),
  (csp('OAYES/S5/C5462/P31369153/Tphoto/IDc1a7de01-0000-0500-0000-00001accb7ea.jpg'),'Quarto')],
 algesrio=[(csp('OAYES/S5/C3796/P31370251/Tphoto/ID0bacde01-0000-0500-0000-00001acd2611.jpg'),'Sala'),
  (csp('OAYES/S5/C3796/P31370251/Tphoto/ID0bacde01-0000-0500-0000-00001acd262c.jpg'),'Estrutura pombalina original à vista'),
  (csp('OAYES/S5/C3796/P31370251/Tphoto/ID0bacde01-0000-0500-0000-00001acd2608.jpg'),'Vista rio'),
  (csp('OAYES/S5/C3796/P31370251/Tphoto/ID0bacde01-0000-0500-0000-00001acd265c.jpg'),'Cozinha'),
  (csp('OAYES/S5/C3796/P31370251/Tphoto/ID0bacde01-0000-0500-0000-00001acd2661.jpg'),'Cozinha'),
  (csp('OAYES/S5/C3796/P31370251/Tphoto/ID0bacde01-0000-0500-0000-00001acd266a.jpg'),'Planta')],
 madragoa=[(csp('OAYES/S5/C1320/P29285166/Tphoto/ID2edbbe01-0000-0500-0000-0000185cb4a5.jpg'),'Sala'),
  (csp('OAYES/S5/C1320/P29285166/Tphoto/ID2edbbe01-0000-0500-0000-0000185cb4a8.jpg'),'Vista rio'),
  (csp('OAYES/S5/C1320/P29285166/Tphoto/ID2edbbe01-0000-0500-0000-0000185cb4c3.jpg'),'Cozinha'),
  (csp('OAYES/S5/C1320/P29285166/Tphoto/ID2edbbe01-0000-0500-0000-0000185cb49b.jpg'),'Sala'),
  (csp('OAYES/S5/C1320/P29285166/Tphoto/ID2edbbe01-0000-0500-0000-0000186987c3.jpg'),'Planta')],
 trinas=[(csp('OAYES/S5/C9984/P31004269/Tphoto/ID6d16d901-0000-0500-0000-00001a58d5f2.jpg'),'Sala'),
  (csp('OAYES/S5/C9984/P31004269/Tphoto/ID6d16d901-0000-0500-0000-00001a58d5f9.jpg'),'Varanda'),
  (csp('OAYES/S5/C9984/P31004269/Tphoto/ID6d16d901-0000-0500-0000-00001a58d5fb.jpg'),'Cozinha'),
  (csp('OAYES/S5/C9984/P31004269/Tphoto/ID6d16d901-0000-0500-0000-00001a58d5fc.jpg'),'Cozinha'),
  (csp('OAYES/S5/C9984/P31004269/Tphoto/ID6d16d901-0000-0500-0000-00001a58d609.jpg'),'Vista')],
)
for h in HOUSES:
    if h['id'] in NEWPH:
        h['photos']=[u for u,c in NEWPH[h['id']]]; h['caps']=[c for u,c in NEWPH[h['id']]]
for h in HOUSES:
    if h['id']=='algesrio': h['why']=['Vista sobre o Tejo e muita luz.','A estrutura pombalina original de madeira está à vista: um detalhe raro e cheio de carácter.','Duas salas que se podem unir numa sala grande, perto da estação de Algés.']
    if h['id']=='boahora': h['line']='T2 · 89 m² · varanda com vista'
NOPLAN={'bica':'Planta a pedir à agência.','boahora':'Planta a pedir à agência.','trinas':'Planta a pedir à agência.','borja':'Planta a pedir ao proprietário.'}
for h in HOUSES:
    if h['id'] in NOPLAN: h['facts']=h['facts']+[('Planta',NOPLAN[h['id']])]
AG=dict(casimiro='CENTURY21 Polo Central II',bica='KW Sol Oeiras',boahora='KW Área',esperanca='RB Real Estate',marques='Open Book, JLL, Dils, Independent Brokers',boavista="Porta da Frente Christie's",becoolival='RE/MAX Siimgroup',algesrio='KW Ábaco',madragoa='JLL Residential',saobento='Engel & Völkers · onze listing',borja='Particular · Nuno · mogelijk ook Knight Frank',trinas='Wanted Real Estate')
for h in HOUSES: h['agency']=AG[h['id']]

# 15/11: back in, Pascale talked to them and they may reconsider
_IDL='https://img4.idealista.pt/blur/WEB_DETAIL/0/id.pro.pt.image.master/'
IDL=_IDL
_R1=[
  dict(id='santos', n=1, name='Santos-o-Velho, Madragoa', price='645 000 €', state='Pronta a habitar', ready=True,
       line='T2 · 100 m² · 3.º andar com elevador',
       photos=[IDL+'04/25/85/335413009.jpg', IDL+'a4/c4/9c/335413014.jpg', IDL+'64/7d/b8/335413013.jpg', IDL+'c6/63/c9/335413028.jpg',
               IDL+'3e/f0/a9/335413012.jpg', IDL+'d0/ea/52/335413017.jpg', IDL+'f8/63/bf/335413015.jpg', IDL+'52/91/6f/335413010.jpg'],
       link='https://www.idealista.pt/imovel/35466924/',
       why=['Prédio antigo com charme, todo reabilitado, e com elevador.',
            'Sala cheia de luz, com vista sobre o rio.',
            'Cozinha aberta para a sala, que pode fechar com portadas brancas quando quiserem.'],
       fit=[('ok','Cozinha aberta'),('ok','Muita luz'),('ok','2 casas de banho'),('mid','645 000 €, um pouco acima dos 633 000 €')],
       note='Fica em Santos, um pouco mais longe de onde vivem agora do que as outras.',
       facts=[('Área','100 m² área bruta'),('Quartos','2, um em suite com closet'),('Casas de banho','2, ambas com banheira'),
              ('Piso','3.º, com elevador'),('Exterior','Vista rio'),('Estado','Remodelado, pronto a habitar')],
       pin=(700,392), walk='Santos-o-Velho, morada exata a confirmar', maps='Santos-o-Velho, Lisboa'),
  dict(id='olival', n=2, name='Rua do Olival, Lapa', price='650 000 €', state='Pronta a habitar', ready=True,
       line='T2 duplex · 3.º andar sem elevador · vista rio',
       photos=[IDL+'9c/2c/41/332085202.jpg', IDL+'a7/b5/34/332085164.jpg', IDL+'72/87/5d/332085179.jpg', IDL+'dd/ec/d6/332085177.jpg',
               IDL+'b7/7e/88/332085182.jpg', IDL+'96/21/6e/332085224.jpg', IDL+'73/94/b1/332085186.jpg', IDL+'92/82/eb/332085193.jpg'],
       link='https://www.idealista.pt/imovel/35418249/',
       why=['Sala de 48 m² com a cozinha integrada, exatamente o que me descreveram.',
            'No piso de cima, uma suite de cerca de 43 m². Vista sobre o rio.',
            'O preço acabou de baixar de 690 000 € para 650 000 €.'],
       fit=[('ok','Cozinha aberta'),('ok','Sala luminosa'),('ok','2 casas de banho'),('ok','Perto de onde vivem')],
       note='O preço por m² é baixo para a Lapa. Se gostarem, verificamos primeiro a documentação. Terceiro andar sem elevador.',
       facts=[('Área','A confirmar na documentação'),('Quartos','2'),('Casas de banho','2'),
              ('Piso','3.º, sem elevador, duplex'),('Construção','1988'),('Estado','Pronto a habitar')],
       pin=(545,434), walk='cerca de 6 min a pé de onde vivem', maps='Rua do Olival, Lisboa'),
  ]
for d in _R1:
    d.pop('n',None);d.pop('pin',None);d.pop('walk',None)
    if d['id']=='santos':
        d['note']='Na primeira seleção acharam que faltava personalidade. Volto a mostrar porque cumpre muito do essencial: cozinha aberta, luz, vista rio e elevador. Só dois quartos.'
    if d['id']=='olival':
        d['note']='Na primeira seleção acharam a sala pequena para o quarto grande. Peço a planta: com obras ligeiras a sala pode crescer. Só dois quartos, terceiro andar sem elevador.'
        d['link']='https://www.idealista.pt/imovel/35418249/'
    HOUSES.append(d)
GEO.update(santos=(38.7079,-9.1572),olival=(38.7058,-9.1650))
AREA.update(santos=100,olival=110)
AG.update(santos='Agência a confirmar, anúncio Idealista',olival='Agência a confirmar, anúncio Idealista')
for h in HOUSES:
    h['geo']=GEO[h['id']];h['agency']=AG[h['id']]
    pr=int(''.join(c for c in h['price'] if c.isdigit()));h['ppm']=f"{round(pr/AREA[h['id']]):,}".replace(',',' ')+' €/m²'
for h in HOUSES:
    if h['id']=='olival': h['ppm']='€/m² a confirmar'
for h in HOUSES:
    if h['id']=='olival': h['agency']='RE/MAX Telheiras · agente 969 003 714'

# 19/11 weekly screening: new house
_B7=dict(id='boahora7',name='Calçada da Boa Hora 7, Junqueira',price='795 000 €',state='Pronta a habitar',ready=True,
  line='T3 · 128 m² · 2.º andar · varanda com vista rio',
  photos=[IDL+x for x in ['db/4b/f2/333736704.jpg','d7/8f/ec/333736500.jpg','9e/ee/86/333736555.jpg','cf/f3/14/333736642.jpg','1a/6e/2b/333736703.jpg','7c/f3/a5/333736503.jpg','e6/f1/6e/333736641.jpg','03/e5/cb/333736502.jpg']],
  caps=['Sala','Varanda com vista rio','Cozinha','Cozinha aberta para a sala','Sala','Sala de jantar','Quarto','Vista'],
  link='https://www.idealista.pt/imovel/35449911/',
  why=['Tetos altos, soalho de madeira e detalhes originais, renovado em 2020 com cuidado.','Sala grande e luminosa, com a cozinha integrada por portas de correr: aberta ou fechada, como quiserem.','Varanda ampla com vista sobre o rio, o MAAT e a ponte, numa rua calma perto de Belém e do comboio.'],
  fit=[('ok','Pé-direito alto e carácter'),('ok','Cozinha semiaberta para a sala'),('ok','3 quartos, 2 casas de banho'),('mid','795 000 € sem obras: no limite do orçamento')],
  note='Venda direta do proprietário, que pede para não ser contactado por agências: confirmo primeiro se aceita trabalhar comigo. 2.º andar sem elevador. Planta a pedir.',
  facts=[('Área','128 m² área bruta'),('Quartos','3'),('Casas de banho','2'),('Piso','2.º, sem elevador'),('Exterior','Varanda com vista rio'),('Estado','Renovado em 2020'),('Planta','Planta a pedir ao proprietário.')],
  maps='Calçada da Boa Hora 7, Lisboa')
HOUSES.append(_B7)
GEO.update(boahora7=(38.69985,-9.19195)); AREA.update(boahora7=128); AG.update(boahora7='Particular · Dimi, via Idealista')
for h in HOUSES:
    if h['id']=='boahora7':
        h['geo']=GEO['boahora7'];h['agency']=AG['boahora7'];h['ppm']=f"{round(795000/128):,}".replace(',',' ')+' €/m²'
    if h['id']=='algesrio':
        h['price']='640 000 €';h['ppm']=f"{round(640000/137):,}".replace(',',' ')+' €/m²'
        h['fit']=[('ok','Vista rio e luz'),('ok','3 quartos, 2 casas de banho'),('mid','Cozinha fechada'),('mid','Rua com muito trânsito')]

# 23/11 search with Pascale: four more houses
_T='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.'
iv2=lambda L:[P+x[len(_T):]+S if x.startswith(_T) else P+x+S for x in L]
_NEW=[
 dict(id='casimiro170',name='Rua Joaquim Casimiro, 170 m², Lapa',price='770 000 €',state='Para atualizar',ready=False,
  line='T3+3 · 170 m² · 3 salas · varandas',
  photos=iv2(['eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmbiI6Im9rMWRvdW81ZmM4NDEtRUNPU1lTVEVNIiwidyI6W3siZm4iOiI2OW5scGE3ZWNxbTcxLUFQVCIsInMiOiIxNiIsImEiOiIwIiwicCI6IjEwLC0xMCJ9XX0.0JR0-jtIfj6UV3drOR_ZUdC6_Hx1t9RAV8V9vBEDPC4','eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmbiI6InBpdHF0eTlkb21oazMtRUNPU1lTVEVNIiwidyI6W3siZm4iOiI2OW5scGE3ZWNxbTcxLUFQVCIsInMiOiIxNiIsImEiOiIwIiwicCI6IjEwLC0xMCJ9XX0.lL1kUKWJm384HaetrjGSW4OwfgXoGixGYlykjTGNnxk','eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmbiI6Imd0a3k1N2YyZ2dtZzEtRUNPU1lTVEVNIiwidyI6W3siZm4iOiI2OW5scGE3ZWNxbTcxLUFQVCIsInMiOiIxNiIsImEiOiIwIiwicCI6IjEwLC0xMCJ9XX0.sxzPR6Ueg7WfmrPbqxLcSInk9eEeWGtapbuu8UA6tlQ','eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmbiI6Inhva2N0cmI1MGU3eC1FQ09TWVNURU0iLCJ3IjpbeyJmbiI6IjY5bmxwYTdlY3FtNzEtQVBUIiwicyI6IjE2IiwiYSI6IjAiLCJwIjoiMTAsLTEwIn1dfQ.RYBDCwqx2nEyKdibl5HOIMaHx4SlKI-hgEuwTw8C-ms','eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmbiI6ImhjNDBhNmpodjl6NjMtRUNPU1lTVEVNIiwidyI6W3siZm4iOiI2OW5scGE3ZWNxbTcxLUFQVCIsInMiOiIxNiIsImEiOiIwIiwicCI6IjEwLC0xMCJ9XX0.UyNtZAPIjfVP5akje1FgIlYYwZ0sg4sslPZ4gHz2IO4']),
  caps=['Sala','Cozinha','Planta','Varanda','Quarto'],
  link='https://www.imovirtual.com/pt/anuncio/apartamento-t3-3-com-170-m-varandas-e-grande-ID1j9X7',
  why=['170 m² de área bruta privativa: espaço para a família e para o futuro.','Três salas que podem juntar numa sala grande, mais três quartos com boas áreas.','Prédio de traça tradicional na Lapa, perto do Jardim da Estrela e a descer para Santos.'],
  fit=[('ok','Muito espaço, 3 quartos grandes'),('ok','Carácter e varandas'),('mid','Cozinha a abrir para a sala'),('mid','770 000 €: negociar para ter margem para obras')],
  note='KW LEAD partilha a 50% com todas as agências, segundo o anúncio. Confirmar pé-direito e o andar.',
  facts=[('Área','170 m² área bruta privativa'),('Quartos','3, mais 3 salas'),('Casas de banho','2'),('Exterior','Varandas'),('Estado','Pronto a habitar, para atualizar'),('Planta','Planta no anúncio.')],
  maps='Rua Joaquim Casimiro, Lisboa'),
 dict(id='cruzq',name='Largo São João, Cruz Quebrada',price='615 000 €',state='Arrendado',ready=True,
  line='T3 · 120 m² · terraço e varanda · arrendado',
  photos=[IDL+x for x in ['cb/d3/69/337513367.jpg','27/41/19/337513369.jpg','b7/58/28/337513377.jpg','c5/df/22/337513358.jpg','42/b3/22/337513336.jpg']],
  caps=['Sala','Sala de jantar','Interior','Interior','Interior'],
  link='https://www.idealista.pt/imovel/35497881/',
  why=['Junto à estação da Cruz Quebrada e ao rio.','120 m² com terraço e varanda, 2 casas de banho.','Preço mais baixo da seleção, com margem no orçamento.'],
  fit=[('ok','Comboio e rio a pé'),('ok','Terraço e varanda'),('no','Está arrendado, com inquilinos'),('mid','Prédio de 1988, pouco carácter antigo')],
  note='Venda particular, Manel Theotónio. Arrendado com inquilinos: perguntar até quando e se sai livre. Entreplanta sem elevador.',
  facts=[('Área','120 m² área bruta'),('Quartos','3'),('Casas de banho','2'),('Piso','Entreplanta, sem elevador'),('Construção','1988'),('Situação','Arrendado, com inquilinos'),('Planta','Planta a pedir ao proprietário.')],
  maps='Largo São João 1, Cruz Quebrada'),
 dict(id='algesrep',name='Avenida da República, Algés',price='679 000 €',state='Pronta a habitar',ready=True,
  line='T3 · 146 m² · sala de 45 m² · 2 garagens',
  photos=iv2(['eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmbiI6ImMyZzhhOTkwYnI0NjItRUNPU1lTVEVNIiwidyI6W3siZm4iOiI2OW5scGE3ZWNxbTcxLUFQVCIsInMiOiIxNiIsImEiOiIwIiwicCI6IjEwLC0xMCJ9XX0.QQJlCjbBeI7CCPEeVh7_I_UsSq6CqibCKoDEGCI1WdQ','eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmbiI6InhybG9yY2c3ZmoxcjEtRUNPU1lTVEVNIiwidyI6W3siZm4iOiI2OW5scGE3ZWNxbTcxLUFQVCIsInMiOiIxNiIsImEiOiIwIiwicCI6IjEwLC0xMCJ9XX0.O2D5NBu1CmOTzngMEbs16tlvqWuxPNw78ocwE2fWjGs','eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmbiI6ImF0MGIxcjR1end2NzEtRUNPU1lTVEVNIiwidyI6W3siZm4iOiI2OW5scGE3ZWNxbTcxLUFQVCIsInMiOiIxNiIsImEiOiIwIiwicCI6IjEwLC0xMCJ9XX0.8Gdx_h-Yzq02o8va_DbPp67UKRVsmQvVvm0OD0JeJJ8','eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmbiI6IjRnMmQ2Z29mOWFvOTMtRUNPU1lTVEVNIiwidyI6W3siZm4iOiI2OW5scGE3ZWNxbTcxLUFQVCIsInMiOiIxNiIsImEiOiIwIiwicCI6IjEwLC0xMCJ9XX0.hp1JJEMBynpO_U2SbMb72WBO5sBSyLZ3NGRZEu1WJZ0']),
  caps=['Sala de 45 m²','Cozinha','Exterior','Quarto'],
  link='https://www.imovirtual.com/pt/anuncio/apartamento-t3-para-venda-ID1jfd9',
  why=['146 m² com uma sala de 45 m² e muita luz.','Centro de Algés, com comboio, comércio e escolas a pé, vista parcial de rio.','Duas garagens em box, uma delas para o carro elétrico.'],
  fit=[('ok','Muito espaço e sala grande'),('ok','Perto do comboio, 2 garagens'),('no','Prédio de 2000, sem carácter antigo'),('mid','Avenida movimentada')],
  note='RE/MAX Happy. Prédio de 2000 com elevador e aquecimento central.',
  facts=[('Área','146 m²'),('Quartos','3'),('Piso','2.º, com elevador'),('Construção','2000'),('Extras','2 garagens em box, arrecadação'),('Planta','Planta a pedir à agência.')],
  maps='Avenida da República, Algés'),
 dict(id='estrela102',name='Calçada da Estrela, 102 m²',price='620 000 €',state='Pronta a habitar',ready=True,
  line='T3 · 102 m² úteis · 3.º andar · remodelado',
  photos=iv2(['eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmbiI6InRnNGhiZDU5MXZ6ei1FQ09TWVNURU0iLCJ3IjpbeyJmbiI6IjY5bmxwYTdlY3FtNzEtQVBUIiwicyI6IjE2IiwiYSI6IjAiLCJwIjoiMTAsLTEwIn1dfQ.UJGz5nfOHpuhZ4MzpI4pmZksec2gVGwJ8Z-4d8X3ILc','eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmbiI6ImRyNmNkNXVpaGRicTMtRUNPU1lTVEVNIiwidyI6W3siZm4iOiI2OW5scGE3ZWNxbTcxLUFQVCIsInMiOiIxNiIsImEiOiIwIiwicCI6IjEwLC0xMCJ9XX0.P5uOF7dg-dEyhtz3jXsRENfX8M2_6eIhS3GkFXqLqN8','eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmbiI6ImFibm5rNXVpazlpdjEtRUNPU1lTVEVNIiwidyI6W3siZm4iOiI2OW5scGE3ZWNxbTcxLUFQVCIsInMiOiIxNiIsImEiOiIwIiwicCI6IjEwLC0xMCJ9XX0.6d1y9lpJUQbP5g9iuwnF-oRx6BMA_tadq3yja7o5ln4','eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmbiI6Im1yOWFmd2JsMTI5bDEtRUNPU1lTVEVNIiwidyI6W3siZm4iOiI2OW5scGE3ZWNxbTcxLUFQVCIsInMiOiIxNiIsImEiOiIwIiwicCI6IjEwLC0xMCJ9XX0.tqBpJ9Xb7LDkPD16UP3wtAW-FIgmhpx_JJphZEro_fQ']),
  caps=['Sala','Cozinha','Planta','Quarto'],
  link='https://www.imovirtual.com/pt/anuncio/apartamento-t3-102-m-calcada-da-estrela-ID1j9RV',
  why=['Remodelado há 3 anos: canalização, eletricidade e janelas novas.','Sala ampla e muito luminosa, junto ao Jardim da Estrela.','620 000 €: o preço deixa margem no orçamento.'],
  fit=[('ok','Remodelado e luminoso'),('mid','3.º andar sem elevador'),('no','Prédio de 1984, pouco carácter'),('no','Longe do rio e do comboio, rua do elétrico')],
  note='KW LEAD. 102 m² de área útil, área bruta a confirmar.',
  facts=[('Área','102 m² área útil'),('Quartos','3'),('Piso','3.º, sem elevador'),('Construção','1984, remodelado há 3 anos'),('Planta','Planta no anúncio.')],
  maps='Calçada da Estrela, Lisboa'),
]
HOUSES.extend(_NEW)
GEO.update(casimiro170=(38.70618,-9.16705),cruzq=(38.6996,-9.2402),algesrep=(38.703396,-9.231186),estrela102=(38.71255,-9.15608))
AREA.update(casimiro170=170,cruzq=120,algesrep=146,estrela102=102)
AG.update(casimiro170='KW LEAD',cruzq='Particular · Manel Theotónio, via Idealista',algesrep='RE/MAX Happy',estrela102='KW LEAD')
for h in _NEW:
    h['geo']=GEO[h['id']];h['agency']=AG[h['id']]
    p=int(h['price'].replace(' ','').replace('€',''));h['ppm']=f"{round(p/AREA[h['id']]):,}".replace(',',' ')+' €/m²'

# 23/11 Pascale: E&V Santos T5 with river view
_EVU='https://uploadcare.engelvoelkers.com/'
_T5=dict(id='santost5',name='Santos, vista rio, 145 m²',price='770 000 €',state='Pronta a habitar',ready=True,
  line='T5 · 145 m² · 2.º andar · vista rio',
  photos=[_EVU+x+'/-/format/jpeg/-/scale_crop/1440x960/center/-/quality/lighter/' for x in ['b4eb64e8-c4d5-4506-9a62-b8f7fd906299', '0d970b89-fc60-4c07-bbda-c31a3810b0c6', '310868fe-5a8a-4143-8239-198ca9a9136d', '7882dbec-c336-435f-8fc2-b6754f5cb56b', '89ff00be-c4ff-46c1-9bb0-fb28422e5f0b', '47f0af6e-ec0c-4d81-b8bd-83f660f1c5b2', '33dc22d2-e1de-4aaf-b9d2-83344687b03c', 'ac3fdebc-e3ad-4eeb-b90d-a520f549dfa2']],
  caps=['Sala com vista rio','Interior','Interior','Interior','Interior','Interior','Interior','Interior'],
  link='https://www.engelvoelkers.com/pt/pt/exposes/14792c85-7d90-588a-ab55-df10bebf1035',
  why=['Vista frontal de rio na sala e num dos quartos, em pleno bairro de Santos.','145 m² num prédio pombalino com duas entradas, soalho e portadas originais.','Cozinha e duas casas de banho já renovadas, aquecimento nas divisões principais.'],
  fit=[('ok','Localização e vista rio'),('ok','Espaço: 145 m²'),('mid','2 quartos com janela, 3 divisões interiores'),('mid','Elevador a confirmar')],
  note='Imóvel Engel & Völkers, consultor Oscar Baptista. Partilha interna, sem partilha escrita com outra agência. Confirmar elevador e a rua exata.',
  facts=[('Área','145 m²'),('Quartos','2 com janela, mais 3 divisões interiores'),('Casas de banho','2, renovadas'),('Piso','2.º'),('Construção','1937'),('Energia','C'),('Planta','Planta a pedir ao Oscar.')],
  maps='Santos, Lisboa')
HOUSES.append(_T5)
GEO.update(santost5=(38.7072,-9.1585)); AREA.update(santost5=145); AG.update(santost5='Engel & Völkers · Oscar Baptista')
_T5['geo']=GEO['santost5'];_T5['agency']=AG['santost5'];_T5['ppm']=f"{round(770000/145):,}".replace(',',' ')+' €/m²'

# 23/11 Pascale: C21 CasaBela 185 m2 renovation project, plus refs and phones for the call round
_C185=dict(id='casimiro185',name='Rua Joaquim Casimiro, 185 m², para remodelar',price='639 000 €',state='Para remodelar',ready=False,
  line='T4+1 · 185 m² área bruta privativa · traça clássica',
  photos=iv2(['eyJmbiI6Inl1aXRiMmxzamxubC1FQ09TWVNURU0iLCJ3IjpbeyJmbiI6IjY5bmxwYTdlY3FtNzEtQVBUIiwicyI6IjE2IiwiYSI6IjAiLCJwIjoiMTAsLTEwIn1dfQ.9180pHr9VxFnNXmXZ1JhXFyLEPTBx0klHt2xnkjwUG0', 'eyJmbiI6InU2dzhvMmRxZG14aC1FQ09TWVNURU0iLCJ3IjpbeyJmbiI6IjY5bmxwYTdlY3FtNzEtQVBUIiwicyI6IjE2IiwiYSI6IjAiLCJwIjoiMTAsLTEwIn1dfQ.IWsVtVhbbXz1L9ae4He1rFbfmq_dqHShv8RLGEj_iaI', 'eyJmbiI6InhnYTBkdXJkNW4zdjMtRUNPU1lTVEVNIiwidyI6W3siZm4iOiI2OW5scGE3ZWNxbTcxLUFQVCIsInMiOiIxNiIsImEiOiIwIiwicCI6IjEwLC0xMCJ9XX0.XsFBk8p0nwDeV2UcqDqLlmDKNGfzzZWnHyz7kB7P3FQ', 'eyJmbiI6IngwMGs2aDdwbXBlcDEtRUNPU1lTVEVNIiwidyI6W3siZm4iOiI2OW5scGE3ZWNxbTcxLUFQVCIsInMiOiIxNiIsImEiOiIwIiwicCI6IjEwLC0xMCJ9XX0.U8iuzkmEUCLDm8ptiznCIoaxuatuFy9uxN5QiSLtXPQ', 'eyJmbiI6IjBmMTFpbzR0dXlocy1FQ09TWVNURU0iLCJ3IjpbeyJmbiI6IjY5bmxwYTdlY3FtNzEtQVBUIiwicyI6IjE2IiwiYSI6IjAiLCJwIjoiMTAsLTEwIn1dfQ.QD7M7UNSRFgl86dQtjeD-rfAxHnuQExXQDZSKHJk7oY', 'eyJmbiI6IjJxdHM2bmQwNW53NjMtRUNPU1lTVEVNIiwidyI6W3siZm4iOiI2OW5scGE3ZWNxbTcxLUFQVCIsInMiOiIxNiIsImEiOiIwIiwicCI6IjEwLC0xMCJ9XX0.h4gUQmjekYJuXoAfquRmFNEYiJnRK5Nv-e65iFhd_yY']),
  caps=['Prédio','Sala','Sala','Sala','Sala','Corredor'],
  link='https://www.imovirtual.com/pt/anuncio/185-m-na-estrela-apartamento-de-traca-classica-para-remodelar-ID1iSML',
  why=['185 m² de área bruta privativa: o grande projeto de remodelação, à medida deles.','Tetos altos, soalho de madeira, duas salas e cinco divisões.','Prédio de 1951 com obras estruturais profundas há menos de 10 anos.'],
  fit=[('ok','Muito espaço para o futuro'),('ok','Preço baixo por m²: margem para obras'),('mid','Obras completas a orçar'),('mid','Andar e elevador a confirmar')],
  note='Century 21 CasaBela, Saúl Ribeiro. Provavelmente o mesmo apartamento que a RE/MAX Siimgroup anuncia a 725 000 €: aqui está 86 000 € mais barato.',
  facts=[('Área','185 m² área bruta privativa'),('Divisões','2 salas e 5 divisões'),('Construção','1951, obras estruturais há menos de 10 anos'),('Estado','Para remodelar'),('Planta','Planta no anúncio.')],
  maps='Rua Joaquim Casimiro, Lisboa')
HOUSES.append(_C185)
GEO.update(casimiro185=(38.705498,-9.167187)); AREA.update(casimiro185=185); AG.update(casimiro185='Century 21 CasaBela')
_C185['geo']=GEO['casimiro185'];_C185['agency']=AG['casimiro185'];_C185['ppm']=f"{round(639000/185):,}".replace(',',' ')+' €/m²'
# call round 23/11: [office called, agent called]
DONE={'casimiro170':[1,0],'estrela102':[1,0],'algesrio':[1,0],'madragoa':[1,0]}
# contact card per house: office, reference, office phone, agent, agent phone, tip
CONTACT={
 'casimiro170':('KW LEAD','KWPT-027353','211 977 898','Catarina Gabriel','913 748 118',''),
 'estrela102':('KW LEAD','KWPT-034228','211 977 898','Lourdes Santos','917 546 499','Escritório confirmou partilha por telefone, falta por escrito'),
 'algesrio':('KW Ábaco','KWPT-038048','217 920 620','António Faria Blanc','917 221 639',''),
 'casimiro185':('Century 21 CasaBela','C0506-00787','210 207 923','Saúl Ribeiro','',''),
 'casimiro':('Century 21 Polo Central II','C0492-00176','210 207 655','','',''),
 'algesrep':('RE/MAX Happy','124991002-72','308 803 763','','',''),
 'becoolival':('RE/MAX Siimgroup','120521520-298','','','','Provavelmente o mesmo que a C21 CasaBela, 86 000 € mais caro'),
 'olival':('RE/MAX Telheiras','120181165-409','218 763 674','','969 003 714',''),
 'madragoa':('JLL Residential','96142','215 564 203','','','23/11: disponível, parceria possível. Para visitar, ligar de novo para a JLL com a ref 96142'),
 'boavista':("Porta da Frente Christie's",'PF40846','210 205 683','','',''),
 'santos':('One Advice Real Estate','Idealista 35466924','210 229 389','','',''),
 'boahora7':('Particular','Idealista 35449911','','Dimi','','Pelo chat do Idealista'),
 'cruzq':('Particular','Idealista 35497881','','Manel Theotónio','','Pelo chat do Idealista'),
 'santost5':('Engel & Völkers','W-049HVO','','Oscar Baptista','','Só ligar se tiverem interesse'),
}
# 23/11 Claude's proposal with Pascale: 2 to renovate, 2 nearby, 2 further
SUG={'casimiro185':('Voorstellen','Renoveren · nr. 1, alles klopt'),
 'madragoa':('Voorstellen','Renoveren · alleen met een lagere prijs'),
 'casimiro':('Voorstellen','Dichtbij, instapklaar · open ruimte, plafonds, patio'),
 'santost5':('Voorstellen','Dichtbij · rivierzicht, maar 2 echte slaapkamers'),
 'algesrio':('Voorstellen','Verder, bij de trein · rivierzicht, ruimte voor werken'),
 'boahora7':('Voorstellen','Verder, bij de trein · op hun limiet, eigenaar wil geen makelaars'),
 'casimiro170':('Twijfel','Reserve · 770k laat weinig over voor werken'),
 'algesrep':('Twijfel','Reserve · veel ruimte, weinig karakter'),
 'boavista':('Twijfel',"Reserve · alleen als Christie's deelt"),
 'becoolival':('Niet voorstellen','Niet · zelfde flat als nr. 1, 86 000 € duurder'),
 'estrela102':('Niet voorstellen','Niet · tram, weinig karakter, ver van de rivier'),
 'cruzq':('Niet voorstellen','Niet · verhuurd, gebouw uit 1988'),
 'olival':('Niet voorstellen','Niet · T2, al gezien'),
 'santos':('Niet voorstellen','Niet · T2, al gezien')}
# 23/11 Belém and Restelo, added after Pascale noticed nothing in Belém
_BT=dict(id='belemt4',name='Belém T4 com logradouro, junto à Torre',price='700 000 €',state='Para remodelar',ready=False,
  line='T4 · 135 m² · logradouro privado · prédio com elevador',
  photos=iv2(['eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmbiI6IjZ4aWVzZHR1Z25pMi1FQ09TWVNURU0iLCJ3IjpbeyJmbiI6IjY5bmxwYTdlY3FtNzEtQVBUIiwicyI6IjE2IiwiYSI6IjAiLCJwIjoiMTAsLTEwIn1dfQ.yT9h2k95osVCDB_cJS_6-Cx5QmEC9FgUESyFy35x0Pk','eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmbiI6ImVhbjAwbGVjMjd3ai1FQ09TWVNURU0iLCJ3IjpbeyJmbiI6IjY5bmxwYTdlY3FtNzEtQVBUIiwicyI6IjE2IiwiYSI6IjAiLCJwIjoiMTAsLTEwIn1dfQ.6bLvJXv1sO3Ww_m8xhM_MXm8HL38Q32yWjuhnXFC2Lk','eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmbiI6Imp3ZGtqajRjeHBrdjEtRUNPU1lTVEVNIiwidyI6W3siZm4iOiI2OW5scGE3ZWNxbTcxLUFQVCIsInMiOiIxNiIsImEiOiIwIiwicCI6IjEwLC0xMCJ9XX0.dDMpfQeCnwE3AekLOb7L6MlDS2Xzb5vtP3_13-HelRw','eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmbiI6InJ4bGYweml3NW5lNDEtRUNPU1lTVEVNIiwidyI6W3siZm4iOiI2OW5scGE3ZWNxbTcxLUFQVCIsInMiOiIxNiIsImEiOiIwIiwicCI6IjEwLC0xMCJ9XX0.f52Uuzx4JrWMAWNA6XJgYgYCwFGS2N1OINI0bfKF4KU','eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmbiI6Im1wZTc1eWN3MjA4bDMtRUNPU1lTVEVNIiwidyI6W3siZm4iOiI2OW5scGE3ZWNxbTcxLUFQVCIsInMiOiIxNiIsImEiOiIwIiwicCI6IjEwLC0xMCJ9XX0.uj0m9EgrswDrgBoDyKuMxiSPmoDre75TSbNeq88yrl0','eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmbiI6IjgyOXd5dnF5b2wxMzItRUNPU1lTVEVNIiwidyI6W3siZm4iOiI2OW5scGE3ZWNxbTcxLUFQVCIsInMiOiIxNiIsImEiOiIwIiwicCI6IjEwLC0xMCJ9XX0.qnuTRPM46eKCnq8IPD4PzgQlZlL-zCx0Cg6dArUgpjk']),
  caps=['Logradouro','Sala','Cozinha','Varanda','Quarto','Exterior'],
  link='https://www.imovirtual.com/pt/anuncio/t4-com-135m2-e-logradouro-privado-belem-home-p-ID1j97V',
  why=['A dois passos da Torre de Belém, do rio e da estação de comboio de Belém.','135 m² e um logradouro privado: espaço para a família e para estar lá fora.','Para remodelar por inteiro: abrir a sala e a cozinha, criar uma suite, tudo à medida deles.'],
  fit=[('ok','Localização junto ao rio e ao comboio'),('ok','4 quartos e logradouro privado'),('mid','Obras completas: 700 000 € mais obras passa os 800 000 €'),('mid','Negociar para perto de 650 000 €')],
  note='KW LEAD, Sandra Ramos. Exclusivo, partilha 50/50 com todas as agências, segundo o anúncio. Terraço comum no topo do prédio.',
  facts=[('Área','135 m², logradouro privado'),('Quartos','4'),('Construção','1963, prédio com elevador'),('Energia','C'),('Estado','Para remodelar por inteiro'),('Planta','Planta a pedir à agência.')],
  maps='Travessa do Arco da Torre, Belém')
_TV=dict(id='tristao',name='Rua Tristão Vaz 31, Restelo',price='625 000 €',state='Pronta a habitar',ready=True,
  line='T3 · 106 m² · 6.º e último andar · 3 varandas',
  photos=iv2(['eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmbiI6InBndGV2aWdsNGFyZTMtRUNPU1lTVEVNIiwidyI6W3siZm4iOiI2OW5scGE3ZWNxbTcxLUFQVCIsInMiOiIxNiIsImEiOiIwIiwicCI6IjEwLC0xMCJ9XX0.L2UpdtxWycG3RpHddOrcooNisQetqTk4MmjH6nwzOgE','eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmbiI6InhmMjR3aHJ4bjh5eDItRUNPU1lTVEVNIiwidyI6W3siZm4iOiI2OW5scGE3ZWNxbTcxLUFQVCIsInMiOiIxNiIsImEiOiIwIiwicCI6IjEwLC0xMCJ9XX0.tlWMeMVpDTatXpYJ2GPE3Tl6WE9IQVkbyJx7sB3ooN4','eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmbiI6InhvdWl1dWpma2JxNDEtRUNPU1lTVEVNIiwidyI6W3siZm4iOiI2OW5scGE3ZWNxbTcxLUFQVCIsInMiOiIxNiIsImEiOiIwIiwicCI6IjEwLC0xMCJ9XX0.Ku59rYUGVDBBB1Jpqerz5RyAMlc7yIqiUm6dGvsuMMY','eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmbiI6Im4ydXZob3Z6MzU4cTMtRUNPU1lTVEVNIiwidyI6W3siZm4iOiI2OW5scGE3ZWNxbTcxLUFQVCIsInMiOiIxNiIsImEiOiIwIiwicCI6IjEwLC0xMCJ9XX0.lfMzIYnY2TWJTiWB-Nh-6PwbvMZs5HZ2yIxFvDXFHFE','eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmbiI6IjZ0ZzNhYnh6NWdlcjEtRUNPU1lTVEVNIiwidyI6W3siZm4iOiI2OW5scGE3ZWNxbTcxLUFQVCIsInMiOiIxNiIsImEiOiIwIiwicCI6IjEwLC0xMCJ9XX0.Dh8htTxX55rtngIsY6lj3fQBFaVSuPRYMbDxVsT81Ho']),
  caps=['Vista','Sala','Sala','Varanda','Sala'],
  link='https://www.imovirtual.com/pt/anuncio/t3-remodelado-106-m-ultimo-piso-3-varanda-ID1jc20',
  why=['Último andar com três frentes: luz o dia todo e privacidade.','Vista desafogada sobre o rio e o mar a partir de duas das três varandas.','Totalmente remodelado, pronto a habitar, deixa margem no orçamento.'],
  fit=[('ok','Luz e vista rio'),('ok','Remodelado, 625 000 €'),('mid','Prédio de 1972, pouco carácter antigo'),('mid','1 casa de banho mais 1 de serviço, a subir da estação')],
  note='KW Select, Gonçalo Freitas. Restelo, cerca de 15 minutos a pé da estação de Belém.',
  facts=[('Área','106 m² área bruta privativa, mais 8 m² de varandas'),('Quartos','3'),('Casas de banho','1 completa e 1 de serviço'),('Piso','6.º e último'),('Construção','1972'),('Planta','Planta no anúncio.')],
  maps='Rua Tristão Vaz 31, Lisboa')
for _h,_g,_a,_p in ((_BT,(38.69466,-9.21593),135,700000),(_TV,(38.7075,-9.20605),106,625000)):
    HOUSES.append(_h);_h['geo']=_g;_h['agency']='KW LEAD' if _h is _BT else 'KW Select';_h['ppm']=f"{round(_p/_a):,}".replace(',',' ')+' €/m²'
CONTACT['belemt4']=('KW LEAD','KWPT-038224','211 977 898','Sandra Ramos','','Exclusivo, partilha 50/50 com todas as agências')
CONTACT['tristao']=('KW Select','KWPT-040339','','Gonçalo Freitas','','')
SUG['belemt4']=('Niet voorstellen','Niet · 700 000 € plus werken is 835 000 € of meer')
SUG['tristao']=('Twijfel','Reserve verder · licht en rivierzicht, weinig karakter')
# 12:09 status after the Calçada test
SUG.update({'algesrio':('Voorstellen','Verder, bij de trein · beter dan de Calçada: 137 m², rivierzicht'),
 'casimiro185':('Voorstellen','Renoveren · alleen met bod rond 550 000–580 000 € en werken in fases'),
 'casimiro':('Twijfel','Te checken · verdieping vragen, gelijkvloers is nee'),
 'boahora7':('Twijfel','Wacht op Dimi · ja is voorstellen, nee is niet'),
 'madragoa':('Twijfel','Reserve · 95 000 € meer dan de Calçada en nog werken'),
 'santost5':('Twijfel','Reserve · maar 2 echte slaapkamers, 770 000 €')})
