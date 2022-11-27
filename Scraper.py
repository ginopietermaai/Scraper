import html2text
from bs4 import BeautifulSoup

html = r"""<table>
<tbody>
<tr>
<td><span><strong><u><span><span><span><span>Elektrisch / Geel kenteken</span></span></span></span></u></strong></span></td>
<td><span><strong><u><span><span>Bijtelling</span></span></u></strong></span></td>
<td><span><strong><u><span><span>Fiscale waarde</span></span></u></strong></span></td>
<td><span><strong><u><span><span>Kenteken</span></span></u></strong></span></td>
<td><span><strong><u><span><span>&nbsp;Kilometerstand&nbsp;</span></span></u></strong></span></td>
<td><span><strong><u><span><span>kleur ext.</span></span></u></strong></span></td>
</tr>
<tr>
<td><span><span><span><span><span>Mazda MX-30 E-Sky 35,5kWh First Ed.</span></span></span></span></span></td>
<td><span><span><span><span><span>8%</span></span></span></span></span></td>
<td><span><span><span><span><span>33899</span></span></span></span></span></td>
<td><span><span><span><span><span>K621JD</span></span></span></span></span></td>
<td><span><span><span><span><span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 11.000</span></span></span></span></span></td>
<td><span><span><span><span><span>Jet Black Mica</span></span></span></span></span></td>
</tr>
<tr>
<td><span><span><span><span><span>Hyundai Ioniq EV Premium 38.3 kWh</span></span></span></span></span></td>
<td><span><span><span><span><span>8%</span></span></span></span></span></td>
<td><span><span><span><span><span>40567</span></span></span></span></span></td>
<td><span><span><span><span><span>J042RT</span></span></span></span></span></td>
<td><span><span><span><span><span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 37.200</span></span></span></span></span></td>
<td><span><span><span><span><span>Electric shadow (grijs)</span></span></span></span></span></td>
</tr>
<tr>
<td><span><span><span><span><span>Audi Q4 e-tron 40 La.Ed.S Competit.</span></span></span></span></span></td>
<td><span><span><span><span><span>17%</span></span></span></span></span></td>
<td><span><span><span><span><span>72690</span></span></span></span></span></td>
<td><span><span><span><span><span>N042SN</span></span></span></span></span></td>
<td><span><span><span><span><span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 29.904</span></span></span></span></span></td>
<td><span><span><span><span><span>Kieselgrijs (C2C2)</span></span></span></span></span></td>
</tr>
<tr>
<td><span><strong><u><span><span><span><span>A-klasse</span></span></span></span></u></strong></span></td>
<td><span><span><span><span><span></span></span></span></span></span></td>
<td><span><span><span><span><span></span></span></span></span></span></td>
<td><span><span><span><span><span></span></span></span></span></span></td>
<td><span><span><span><span><span>&nbsp;&nbsp;</span></span></span></span></span></td>
<td><span><span><span><span><span></span></span></span></span></span></td>
</tr>
<tr>
<td><span><span><span><span><span>Opel Karl 1.0 120 Jaar Edition</span></span></span></span></span></td>
<td><span><span><span><span><span>22%</span></span></span></span></span></td>
<td><span><span><span><span><span>13598</span></span></span></span></span></td>
<td><span><span><span><span><span>ZL313S</span></span></span></span></span></td>
<td><span><span><span><span><span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 19.906</span></span></span></span></span></td>
<td><span><span><span><span><span>Summit White uni</span></span></span></span></span></td>
</tr>
<tr>
<td><span><span><span><span><span>Kia Picanto 1.0 Comf+ Nav.4-zits</span></span></span></span></span></td>
<td><span><span><span><span><span>22%</span></span></span></span></span></td>
<td><span><span><span><span><span>13785</span></span></span></span></span></td>
<td><span><span><span><span><span>XB741F</span></span></span></span></span></td>
<td><span><span><span><span><span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 62.960</span></span></span></span></span></td>
<td><span><span><span><span><span>Clear white uni</span></span></span></span></span></td>
</tr>
<tr>
<td><span><span><span><span><span>Hyundai i10 1.0 Comfort 4p</span></span></span></span></span></td>
<td><span><span><span><span><span>22%</span></span></span></span></span></td>
<td><span><span><span><span><span>14006</span></span></span></span></span></td>
<td><span><span><span><span><span>G798GV</span></span></span></span></span></td>
<td><span><span><span><span><span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 35.960</span></span></span></span></span></td>
<td><span><span><span><span><span>Aqua sparkling met.</span></span></span></span></span></td>
</tr>
<tr>
<td><span><span><span><span><span>Citroën C1 VTi 72 Shine 5d</span></span></span></span></span></td>
<td><span><span><span><span><span>22%</span></span></span></span></span></td>
<td><span><span><span><span><span>14730</span></span></span></span></span></td>
<td><span><span><span><span><span>ZV141J</span></span></span></span></span></td>
<td><span><span><span><span><span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 60.620</span></span></span></span></span></td>
<td><span><span><span><span><span>lipizan white unilak</span></span></span></span></span></td>
</tr>
<tr>
<td><span><strong><u><span><span><span><span>B-klasse (station)</span></span></span></span></u></strong></span></td>
<td><span><span><span><span><span></span></span></span></span></span></td>
<td><span><span><span><span><span></span></span></span></span></span></td>
<td><span><span><span><span><span></span></span></span></span></span></td>
<td><span><span><span><span><span>&nbsp;&nbsp;</span></span></span></span></span></td>
<td><span><span><span><span><span></span></span></span></span></span></td>
</tr>
<tr>
<td><span><span><span><span><span>Opel Corsa 1.2 75 Edition (nw model)</span></span></span></span></span></td>
<td><span><span><span><span><span>22%</span></span></span></span></span></td>
<td><span><span><span><span><span>18791</span></span></span></span></span></td>
<td><span><span><span><span><span>H618HL</span></span></span></span></span></td>
<td><span><span><span><span><span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 37.892</span></span></span></span></span></td>
<td><span><span><span><span><span>Summit white uni</span></span></span></span></span></td>
</tr>
<tr>
<td><span><span><span><span><span>Renault Clio TCe 90 Intens</span></span></span></span></span></td>
<td><span><span><span><span><span>22%</span></span></span></span></span></td>
<td><span><span><span><span><span>18895</span></span></span></span></span></td>
<td><span><span><span><span><span>TK266S</span></span></span></span></span></td>
<td><span><span><span><span><span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 51.615</span></span></span></span></span></td>
<td><span><span><span><span><span>Wit unilak</span></span></span></span></span></td>
</tr>
<tr>
<td><span><span><span><span><span>Toyota&nbsp; Yaris 1.5 VVT-i Active 5d</span></span></span></span></span></td>
<td><span><span><span><span><span>22%</span></span></span></span></span></td>
<td><span><span><span><span><span>21745</span></span></span></span></span></td>
<td><span><span><span><span><span>K242PN</span></span></span></span></span></td>
<td><span><span><span><span><span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 25.666</span></span></span></span></span></td>
<td><span><span><span><span><span>Cobalt blue met.</span></span></span></span></span></td>
</tr>
<tr>
<td><span><span><span><span><span>Volkswagen Polo 1.0 TSI 70 Highline 5d</span></span></span></span></span></td>
<td><span><span><span><span><span>22%</span></span></span></span></span></td>
<td><span><span><span><span><span>23503</span></span></span></span></span></td>
<td><span><span><span><span><span>TR689H</span></span></span></span></span></td>
<td><span><span><span><span><span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 50.773</span></span></span></span></span></td>
<td><span><span><span><span><span>Orange metallic</span></span></span></span></span></td>
</tr>
<tr>
<td><span><span><span><span><span>Opel Crossland 1.2 Edition</span></span></span></span></span></td>
<td><span><span><span><span><span>22%</span></span></span></span></span></td>
<td><span><span><span><span><span>24897</span></span></span></span></span></td>
<td><span><span><span><span><span>L718FL</span></span></span></span></span></td>
<td><span><span><span><span><span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 39.416</span></span></span></span></span></td>
<td><span><span><span><span><span>Moonstone grey met.</span></span></span></span></span></td>
</tr>
<tr>
<td><span><span><span><span><span>Seat Arona 1.0 TSI 115 X Bs.Int.Aut</span></span></span></span></span></td>
<td><span><span><span><span><span>22%</span></span></span></span></span></td>
<td><span><span><span><span><span>28061</span></span></span></span></span></td>
<td><span><span><span><span><span>TR954B</span></span></span></span></span></td>
<td><span><span><span><span><span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 105.074</span></span></span></span></span></td>
<td><span><span><span><span><span>White metallic / Grijs dak</span></span></span></span></span></td>
</tr>
<tr>
<td><span><span><span><span><span>Opel Crossland 1.2 110 Elegance</span></span></span></span></span></td>
<td><span><span><span><span><span>22%</span></span></span></span></span></td>
<td><span><span><span><span><span>29064</span></span></span></span></span></td>
<td><span><span><span><span><span>L151SN</span></span></span></span></span></td>
<td><span><span><span><span><span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 23.606</span></span></span></span></span></td>
<td><span><span><span><span><span>Moonstone grey met.</span></span></span></span></span></td>
</tr>
<tr>
<td><span><strong><u><span><span><span><span>C-klasse (station)</span></span></span></span></u></strong></span></td>
<td><span><span><span><span><span></span></span></span></span></span></td>
<td><span><span><span><span><span></span></span></span></span></span></td>
<td><span><span><span><span><span></span></span></span></span></span></td>
<td><span><span><span><span><span>&nbsp;&nbsp;</span></span></span></span></span></td>
<td><span><span><span><span><span></span></span></span></span></span></td>
</tr>
<tr>
<td><span><span><span><span><span>Skoda Octavia 1.0 TSI 81kW Business Ed. + Hatchb.</span></span></span></span></span></td>
<td><span><span><span><span><span>22%</span></span></span></span></span></td>
<td><span><span><span><span><span>31192</span></span></span></span></span></td>
<td><span><span><span><span><span>L138SF</span></span></span></span></span></td>
<td><span><span><span><span><span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 33.871</span></span></span></span></span></td>
<td><span><span><span><span><span>Titan blue met.</span></span></span></span></span></td>
</tr>
<tr>
<td><span><span><span><span><span>Ford Focus Wagon1.0 125 Titan.Bs.Aut</span></span></span></span></span></td>
<td><span><span><span><span><span>22%</span></span></span></span></span></td>
<td><span><span><span><span><span>31600</span></span></span></span></span></td>
<td><span><span><span><span><span>ZB406F</span></span></span></span></span></td>
<td><span><span><span><span><span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 101.305</span></span></span></span></span></td>
<td><span><span><span><span><span>Chrome blue met.</span></span></span></span></span></td>
</tr>
<tr>
<td><span><span><span><span><span>Opel Astra 1.4T Innovation Aut.</span></span></span></span></span></td>
<td><span><span><span><span><span>22%</span></span></span></span></span></td>
<td><span><span><span><span><span>32247</span></span></span></span></span></td>
<td><span><span><span><span><span>ZR570D</span></span></span></span></span></td>
<td><span><span><span><span><span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 26.224</span></span></span></span></span></td>
<td><span><span><span><span><span>indigo blue unilak</span></span></span></span></span></td>
</tr>
<tr>
<td><span><span><span><span><span>Hyundai Kona 1.6 GDI HEV Premium</span></span></span></span></span></td>
<td><span><span><span><span><span>22%</span></span></span></span></span></td>
<td><span><span><span><span><span>33437</span></span></span></span></span></td>
<td><span><span><span><span><span>J342KB</span></span></span></span></span></td>
<td><span><span><span><span><span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 48.982</span></span></span></span></span></td>
<td><span><span><span><span><span>Galactic grey met.</span></span></span></span></span></td>
</tr>
<tr>
<td><span><span><span><span><span>Hyundai Kona 1.6 GDI HEV Premium</span></span></span></span></span></td>
<td><span><span><span><span><span>22%</span></span></span></span></span></td>
<td><span><span><span><span><span>34232</span></span></span></span></span></td>
<td><span><span><span><span><span>J288KL</span></span></span></span></span></td>
<td><span><span><span><span><span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 13.869</span></span></span></span></span></td>
<td><span><span><span><span><span>Phantom Black parelmoer (MZH)</span></span></span></span></span></td>
</tr>
<tr>
<td><span><span><span><span><span>Mazda 3 SKYACTIV-X 180 Luxury 5d</span></span></span></span></span></td>
<td><span><span><span><span><span>22%</span></span></span></span></span></td>
<td><span><span><span><span><span>34480</span></span></span></span></span></td>
<td><span><span><span><span><span>J112GD</span></span></span></span></span></td>
<td><span><span><span><span><span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 52.857</span></span></span></span></span></td>
<td><span><span><span><span><span>Soul Red Crystal Metallic</span></span></span></span></span></td>
</tr>
<tr>
<td><span><span><span><span><span>Opel Astra ST 1.4T 107 Elegance Aut</span></span></span></span></span></td>
<td><span><span><span><span><span>22%</span></span></span></span></span></td>
<td><span><span><span><span><span>36389</span></span></span></span></span></td>
<td><span><span><span><span><span>H122KJ</span></span></span></span></span></td>
<td><span><span><span><span><span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 37.883</span></span></span></span></span></td>
<td><span><span><span><span><span>nautic blue metallic</span></span></span></span></span></td>
</tr>
<tr>
<td><span><span><span><span><span>Audi A3 35TFSI Lease Edit.Aut. 4d</span></span></span></span></span></td>
<td><span><span><span><span><span>22%</span></span></span></span></span></td>
<td><span><span><span><span><span>36530</span></span></span></span></span></td>
<td><span><span><span><span><span>XV979Z</span></span></span></span></span></td>
<td><span><span><span><span><span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 58.013</span></span></span></span></span></td>
<td><span><span><span><span><span>Brillantzwart uni</span></span></span></span></span></td>
</tr>
<tr>
<td><span><span><span><span><span>Mazda 3 SKYACTIV-X 180 Luxury Aut.5d</span></span></span></span></span></td>
<td><span><span><span><span><span>22%</span></span></span></span></span></td>
<td><span><span><span><span><span>36549</span></span></span></span></span></td>
<td><span><span><span><span><span>G224KV</span></span></span></span></span></td>
<td><span><span><span><span><span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 68.631</span></span></span></span></span></td>
<td><span><span><span><span><span>machine gray metallic</span></span></span></span></span></td>
</tr>
<tr>
<td><span><span><span><span><span>Mercedes-Benz B 180 Business Sol.AMG Aut.</span></span></span></span></span></td>
<td><span><span><span><span><span>22%</span></span></span></span></span></td>
<td><span><span><span><span><span>40369</span></span></span></span></span></td>
<td><span><span><span><span><span>H856JF</span></span></span></span></span></td>
<td><span><span><span><span><span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 31.970</span></span></span></span></span></td>
<td><span><span><span><span><span>Kosmoszwart met.</span></span></span></span></span></td>
</tr>
<tr>
<td><span><strong><u><span><span><span><span>SUV</span></span></span></span></u></strong></span></td>
<td><span><span><span><span><span></span></span></span></span></span></td>
<td><span><span><span><span><span></span></span></span></span></span></td>
<td><span><span><span><span><span></span></span></span></span></span></td>
<td><span><span><span><span><span>&nbsp;&nbsp;</span></span></span></span></span></td>
<td><span><span><span><span><span></span></span></span></span></span></td>
</tr>
<tr>
<td><span><span><span><span><span>Skoda Karoq 1.0 TSI Ambition Bus.</span></span></span></span></span></td>
<td><span><span><span><span><span>22%</span></span></span></span></span></td>
<td><span><span><span><span><span>33215</span></span></span></span></span></td>
<td><span><span><span><span><span>XR979K</span></span></span></span></span></td>
<td><span><span><span><span><span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 58.279</span></span></span></span></span></td>
<td><span><span><span><span><span>brilliant silver metallic</span></span></span></span></span></td>
</tr>
<tr>
<td><span><span><span><span><span>Skoda Karoq 1.5 TSI Bus.Edition Aut.</span></span></span></span></span></td>
<td><span><span><span><span><span>22%</span></span></span></span></span></td>
<td><span><span><span><span><span>36145</span></span></span></span></span></td>
<td><span><span><span><span><span>H261GV</span></span></span></span></span></td>
<td><span><span><span><span><span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 81.236</span></span></span></span></span></td>
<td><span><span><span><span><span>Velvet red met.</span></span></span></span></span></td>
</tr>
<tr>
<td><span><span><span><span><span>Renault Gr.Scénic TCe 140 Bose Aut.</span></span></span></span></span></td>
<td><span><span><span><span><span>22%</span></span></span></span></span></td>
<td><span><span><span><span><span>37610</span></span></span></span></span></td>
<td><span><span><span><span><span>TB229Z</span></span></span></span></span></td>
<td><span><span><span><span><span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 86.840</span></span></span></span></span></td>
<td><span><span><span><span><span>metaallak noir etoilé (GNE)</span></span></span></span></span></td>
</tr>
<tr>
<td><span><span><span><span><span>Opel Grandland X 1.2T 96 Innov.Aut.</span></span></span></span></span></td>
<td><span><span><span><span><span>22%</span></span></span></span></span></td>
<td><span><span><span><span><span>42640</span></span></span></span></span></td>
<td><span><span><span><span><span>J340TS</span></span></span></span></span></td>
<td><span><span><span><span><span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 58.483</span></span></span></span></span></td>
<td><span><span><span><span><span>diamond black metallic</span></span></span></span></span></td>
</tr>
<tr>
<td><span><span><span><span><span>Skoda Karoq 1.5 TSI Style Bus.Aut.</span></span></span></span></span></td>
<td><span><span><span><span><span>22%</span></span></span></span></span></td>
<td><span><span><span><span><span>43605</span></span></span></span></span></td>
<td><span><span><span><span><span>G106BR</span></span></span></span></span></td>
<td><span><span><span><span><span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 103.084</span></span></span></span></span></td>
<td><span><span><span><span><span>Quartz grey met.</span></span></span></span></span></td>
</tr>
<tr>
<td><span><span><span><span><span>Toyota&nbsp; RAV4 2.5 Hybrid 2WD Executive</span></span></span></span></span></td>
<td><span><span><span><span><span>22%</span></span></span></span></span></td>
<td><span><span><span><span><span>48670</span></span></span></span></span></td>
<td><span><span><span><span><span>ZP496S</span></span></span></span></span></td>
<td><span><span><span><span><span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 47.435</span></span></span></span></span></td>
<td><span><span><span><span><span>zircon silver metallic</span></span></span></span></span></td>
</tr>
<tr>
<td><span><strong><u><span><span><span><span>Premium/Luxe station</span></span></span></span></u></strong></span></td>
<td><span><span><span><span><span></span></span></span></span></span></td>
<td><span><span><span><span><span></span></span></span></span></span></td>
<td><span><span><span><span><span></span></span></span></span></span></td>
<td><span><span><span><span><span>&nbsp;&nbsp;</span></span></span></span></span></td>
<td><span><span><span><span><span></span></span></span></span></span></td>
</tr>
<tr>
<td><span><span><span><span><span>BMW 318i Tour.M Sport CL Aut.</span></span></span></span></span></td>
<td><span><span><span><span><span>22%</span></span></span></span></span></td>
<td><span><span><span><span><span>41275</span></span></span></span></span></td>
<td><span><span><span><span><span>ZG364F</span></span></span></span></span></td>
<td><span><span><span><span><span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 73.188</span></span></span></span></span></td>
<td><span><span><span><span><span>mineralgrau metallic</span></span></span></span></span></td>
</tr>
<tr>
<td><span><span><span><span><span>Mercedes-Benz CLA 180 d Bus.Sol.Prog.Aut.</span></span></span></span></span></td>
<td><span><span><span><span><span>22%</span></span></span></span></span></td>
<td><span><span><span><span><span>41706</span></span></span></span></span></td>
<td><span><span><span><span><span>H608JB</span></span></span></span></span></td>
<td><span><span><span><span><span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 95.838</span></span></span></span></span></td>
<td><span><span><span><span><span>Berg grijs met.</span></span></span></span></span></td>
</tr>
<tr>
<td><span><span><span><span><span>Mercedes-Benz A 180 Business Sol.AMG Aut.</span></span></span></span></span></td>
<td><span><span><span><span><span>22%</span></span></span></span></span></td>
<td><span><span><span><span><span>43722</span></span></span></span></span></td>
<td><span><span><span><span><span>K372VZ</span></span></span></span></span></td>
<td><span><span><span><span><span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 101.261</span></span></span></span></span></td>
<td><span><span><span><span><span>Mojavezilver met.</span></span></span></span></span></td>
</tr>
<tr>
<td><span><span><span><span><span>Mercedes-Benz CLA SB 180 Bus.Sol.Aut.</span></span></span></span></span></td>
<td><span><span><span><span><span>22%</span></span></span></span></span></td>
<td><span><span><span><span><span>43874</span></span></span></span></span></td>
<td><span><span><span><span><span>H648KT</span></span></span></span></span></td>
<td><span><span><span><span><span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 63.252</span></span></span></span></span></td>
<td><span><span><span><span><span>Poolwit unilak</span></span></span></span></span></td>
</tr>
<tr>
<td><span><span><span><span><span>Volkswagen Passat Var.TSI 110 Hi.Bs.R Aut</span></span></span></span></span></td>
<td><span><span><span><span><span>22%</span></span></span></span></span></td>
<td><span><span><span><span><span>45501</span></span></span></span></span></td>
<td><span><span><span><span><span>ZH501P</span></span></span></span></span></td>
<td><span><span><span><span><span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 82.495</span></span></span></span></span></td>
<td><span><span><span><span><span>Pyrit Silver met.</span></span></span></span></span></td>
</tr>
<tr>
<td><span><span><span><span><span>BMW X1 Xdrive 25e High Exe Aut.&nbsp;</span></span></span></span></span></td>
<td><span><span><span><span><span>22%</span></span></span></span></span></td>
<td><span><span><span><span><span>50760</span></span></span></span></span></td>
<td><span><span><span><span><span>N540KX</span></span></span></span></span></td>
<td><span><span><span><span><span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 14.097</span></span></span></span></span></td>
<td><span><span><span><span><span>Schwarz Uni lak</span></span></span></span></span></td>
</tr>
<tr>
<td><span><span><span><span><span>Audi A4 Avant 35TFSI 110 La.ed.Bu.Aut.</span></span></span></span></span></td>
<td><span><span><span><span><span>22%</span></span></span></span></span></td>
<td><span><span><span><span><span>51320</span></span></span></span></span></td>
<td><span><span><span><span><span>H050RN</span></span></span></span></span></td>
<td><span><span><span><span><span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 79.714</span></span></span></span></span></td>
<td><span><span><span><span><span>Brillant zwart unilak</span></span></span></span></span></td>
</tr>
<tr>
<td><span><span><span><span><span>Volvo V60 T5 Momentum Aut.</span></span></span></span></span></td>
<td><span><span><span><span><span>22%</span></span></span></span></span></td>
<td><span><span><span><span><span>51465</span></span></span></span></span></td>
<td><span><span><span><span><span>XT267P</span></span></span></span></span></td>
<td><span><span><span><span><span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 86.327</span></span></span></span></span></td>
<td><span><span><span><span><span>onyx black metallic</span></span></span></span></span></td>
</tr>
<tr>
<td><span><span><span><span><span>BMW 318d Tour.Corporate Exec.</span></span></span></span></span></td>
<td><span><span><span><span><span>22%</span></span></span></span></span></td>
<td><span><span><span><span><span>52342,78</span></span></span></span></span></td>
<td><span><span><span><span><span>G574ZT</span></span></span></span></span></td>
<td><span><span><span><span><span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 72.055</span></span></span></span></span></td>
<td><span><span><span><span><span>Schwarz unilak</span></span></span></span></span></td>
</tr>
<tr>
<td><span><span><span><span><span>BMW X1 sDrive20i Exe Sport Line Aut.</span></span></span></span></span></td>
<td><span><span><span><span><span>22%</span></span></span></span></span></td>
<td><span><span><span><span><span>52436</span></span></span></span></span></td>
<td><span><span><span><span><span>TH753X</span></span></span></span></span></td>
<td><span><span><span><span><span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 61.350</span></span></span></span></span></td>
<td><span><span><span><span><span>Alpinweiss met.</span></span></span></span></span></td>
</tr>
<tr>
<td><span><span><span><span><span>BMW 320i Tour.Corporate Exec.Aut (Nw model)</span></span></span></span></span></td>
<td><span><span><span><span><span>22%</span></span></span></span></span></td>
<td><span><span><span><span><span>52928</span></span></span></span></span></td>
<td><span><span><span><span><span>G280ZP</span></span></span></span></span></td>
<td><span><span><span><span><span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 101.086</span></span></span></span></span></td>
<td><span><span><span><span><span>Zwart unilak</span></span></span></span></span></td>
</tr>
<tr>
<td><span><span><span><span><span>Mercedes-Benz GLC 200 Bus.Sol.Lim.Aut.</span></span></span></span></span></td>
<td><span><span><span><span><span>22%</span></span></span></span></span></td>
<td><span><span><span><span><span>54096</span></span></span></span></span></td>
<td><span><span><span><span><span>G789PT</span></span></span></span></span></td>
<td><span><span><span><span><span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 63.246</span></span></span></span></span></td>
<td><span><span><span><span><span>Wit</span></span></span></span></span></td>
</tr>
<tr>
<td><span><span><span><span><span>Audi A5 SB 40TFSI 140 Sp.SL Ed.Aut</span></span></span></span></span></td>
<td><span><span><span><span><span>22%</span></span></span></span></span></td>
<td><span><span><span><span><span>60268</span></span></span></span></span></td>
<td><span><span><span><span><span>G355DD</span></span></span></span></span></td>
<td><span><span><span><span><span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 78.994</span></span></span></span></span></td>
<td><span><span><span><span><span>daytonagrijs parellak</span></span></span></span></span></td>
</tr>
<tr>
<td><span><span><span><span><span>BMW 530i High Exe Edition Aut. 4d</span></span></span></span></span></td>
<td><span><span><span><span><span>22%</span></span></span></span></span></td>
<td><span><span><span><span><span>76564</span></span></span></span></span></td>
<td><span><span><span><span><span>G720RR</span></span></span></span></span></td>
<td><span><span><span><span><span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 43.720</span></span></span></span></span></td>
<td><span><span><span><span><span>Azuritzschwarz II met.</span></span></span></span></span></td>
</tr>
<tr>
<td><span><span><span><span><span>Audi A6 Avant 45 TDI qu.Bus.Edi.Aut&nbsp;</span></span></span></span></span></td>
<td><span><span><span><span><span>22%</span></span></span></span></span></td>
<td><span><span><span><span><span>100647</span></span></span></span></span></td>
<td><span><span><span><span><span>H850LS</span></span></span></span></span></td>
<td><span><span><span><span><span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 73.874</span></span></span></span></span></td>
<td><span><span><span><span><span>Sohobruin met.</span></span></span></span></span></td>
</tr>
<tr>
<td><span><strong><u><span><span>Bestelbus/grijs kenteken</span></span></u></strong></span></td>
<td><span><span><span><span><span></span></span></span></span></span></td>
<td><span><span><span><span><span></span></span></span></span></span></td>
<td><span><span><span><span><span></span></span></span></span></span></td>
<td><span><span><span><span><span>&nbsp;&nbsp;</span></span></span></span></span></td>
<td><span><span><span><span><span></span></span></span></span></span></td>
</tr>
<tr>
<td><span><span><span><span><span>Renault Kangoo Expr.dCi 90 L1 Comfort</span></span></span></span></span></td>
<td><span><span><span><span><span>22%</span></span></span></span></span></td>
<td><span><span><span><span><span>28732</span></span></span></span></span></td>
<td><span><span><span><span><span>V720ZJ</span></span></span></span></span></td>
<td><span><span><span><span><span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 61.522</span></span></span></span></span></td>
<td><span><span><span><span><span>Zwart metallic</span></span></span></span></span></td>
</tr>
<tr>
<td><span><span><span><span><span>Citroën Berlingo HDi 100 Club 650 4d</span></span></span></span></span></td>
<td><span><span><span><span><span>22%</span></span></span></span></span></td>
<td><span><span><span><span><span>32822</span></span></span></span></span></td>
<td><span><span><span><span><span>VPH71T</span></span></span></span></span></td>
<td><span><span><span><span><span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 9.639</span></span></span></span></span></td>
<td><span><span><span><span><span>Perla Nera Black</span></span></span></span></span></td>
</tr>
<tr>
<td><span><span><span><span><span>Renault Kangoo Expr.ZE L1 33 (incl. accu)</span></span></span></span></span></td>
<td><span><span><span><span><span>8%</span></span></span></span></span></td>
<td><span><span><span><span><span>38512</span></span></span></span></span></td>
<td><span><span><span><span><span>VGV10Z</span></span></span></span></span></td>
<td><span><span><span><span><span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 6.598</span></span></span></span></span></td>
<td><span><span><span><span><span>Blanc Minéral standaardlak</span></span></span></span></span></td>
</tr>
</tbody>
</table>"""
website_content = BeautifulSoup(html, 'html.parser').get_text().replace('\xa0', '').replace('\n\n', '').replace('\n ', '\n')
print(website_content)
#text = html2text.html2text(html).replace(' ', '').replace('||', '\n')
#print(text)



#import requests

#bot = 'https://api.telegram.org/bot5980362577:AAGMqqy4nSZPrxdL6KLboDalAE6DQRJ3z2o/'
    
# send message to telegram  
#parameters = {'chat_id': '5748584641', 'text': 'tester de test'}
#requests.post(bot + 'sendMessage', data=parameters)


#from bs4 import BeautifulSoup
#import requests
 

# get content of website and parse it
#website_request = requests.get('https://arval.nl/public/herinzetlijst/', timeout=5)
#website_content = BeautifulSoup(website_request.content, "html.parser")
    
# extract job description
#container = website_content.find_all(class_ = 'grid-container')[-1]
#table = container.find_all('table')
#f = open('output.txt', 'w')
#f.write(str(table).strip("[']"))
#f.close()

# instantiate options 
#options = webdriver.ChromeOptions() 
 
# run browser in headless mode 
#options.headless = True 
 
# instantiate driver 
#driver = webdriver.Chrome(service=ChromeService( 
#	ChromeDriverManager().install()), options=options) 
 
# load website 
#url = 'https://arval.nl/public/herinzetlijst/' 

# get the entire website content 
#driver.get(url) 
#wait = WebDriverWait(driver, 40)
#wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "grid-container")))


# select elements by class name 
#element = driver.find_elements(By.CLASS_NAME, 'grid-container')[-1] 

#print(element.text)

#https://api.telegram.org/bot5980362577:AAGMqqy4nSZPrxdL6KLboDalAE6DQRJ3z2o/sendMessage?chat_id=5748584641&text=ginoooooo2