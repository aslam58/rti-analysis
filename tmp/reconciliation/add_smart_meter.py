from pathlib import Path
p=Path('tmp/reconciliation/build_summary.py');s=p.read_text()
s=s.replace("subject='Electricity procurement finance infrastructure budgets and rooftop solar'","subject='Electricity procurement finance infrastructure budgets rooftop solar and smart metering'")
s=s.replace("p('Electricity purchases finances network works and rooftop solar',size=12,after=12)","p('Electricity purchases finances network works solar and smart meters',size=12,after=12)")
s=s.replace("C pages 2 to 4. Highlighted extracts follow each finding.","C pages 2 to 4  |  D pages 1 and 2. Highlighted extracts follow each finding.")
s=s.replace("'B page 10  |  Findings 6 and 7')]:","'B page 10  |  Findings 6 and 7'),\n ('The **Rs 383.59 crore smart meter project** note reports billing integration problems and dates that need correction.','D page 1  |  Findings 9 and 10')]:")
s=s.replace("['C','Electricity_document_2.pdf','FPPCA and regulatory costs\\nReply dated 6 February 2026']],widths=", "['C','Electricity_document_2.pdf','FPPCA and regulatory costs\\nReply dated 6 February 2026'],\n ['D','Smart Meter Project_\\nelectricity_document_3.pdf','Smart metering and RDSS loss reduction\\nReporting date not established']],widths=")
s=s.replace("This means receiving equipment was substantially ahead of installing it.')","This means receiving equipment was substantially ahead of installing it. A second RDSS note gives a different snapshot, reconciled in Finding 11.')")
old="p('For a complete financial reconciliation, the department would need to connect quantities purchased and received with recognised costs payments revenue collected and the closing revenue gap. For project performance, it would need dated completion records and measured service or generation results.',size=9.5)"
s=s.replace(old,'')
new=r'''
# SMART METER ADDITION
page('9 Smart metering faced a billing integration obstacle')
p('The new note reports a **Rs 383.59 crore smart metering project** involving PFCCL and Apraava Energy Pvt Ltd. It gives a project award figure rather than an account of payments made. The pages do not supply the total number of meters contracted or an expenditure statement for this component.')
caption('Source D page 1 point 1. The original award amount and contracting parties are shown below. The printed dates are examined in Finding 10.')
image('smart_cost',width=6.7)
p('The note attributes the initial installation approach to opposition to smart meters. It says installations were initially arranged for **government premises new consumers and solar consumers**, alongside replacement of faulty meters across consumer categories.')
p('The note also states that **NIC declined support for connecting the smart metering system with the billing software**. Remotely collected readings were instead arranged for regular sharing with the billing system to generate bills. This describes a workaround; the note does not demonstrate full automated billing integration.')
caption('Source D page 1 points 2b and 2c. The initial installation groups integration obstacle and sharing of readings are highlighted.')
image('smart_billing',width=6.7)
p('**Link to the earlier records.** Government and solar consumers overlap with the earlier solar programme topics, but there is no matching list showing which sites received smart meters. The earlier Urban Division meter replacement counts also cannot be treated as smart meter installation totals because they do not identify the meter type.',size=10)
caption('Related records: B page 7 meter replacement entries and B page 10 solar programme figures; D page 1 point 2b above.')
p('The smart metering component and the Rs 106.54 crore RDSS network works are described separately. Their stated costs should not be combined into an expenditure total.',size=9.8)
caption('Source D page 1 point 1 and page 2 final paragraph; the network works figures are reproduced in Finding 11.')

page('10 Meter rollout and feeder monitoring are different milestones')
p('The note reports an installation milestone of **5 percent of smart meters**, followed by testing arrangements and a claimed go live. It supplies no meter count or clear reporting date for that milestone, so **5 percent cannot be presented as the current completion rate**.')
caption('Source D page 1 point 2e. Both the 5 percent milestone and the printed go live date are highlighted.')
image('smart_milestone',width=6.7)
p('**The printed go live date is invalid.** The note says “31.02.2026”; February has no 31st day. It separately prints the contract date as “3.9.2026” and the inauguration date as “1.03.2026”. A corrected and dated project timeline is needed before the sequence or delivery period can be verified.')
caption('Source D page 1 point 1. Contract and inauguration dates as printed. No corrected date has been assumed.')
image('smart_dates',width=6.7)
p('The note separately claims **100 percent feeder integration with the National Feeder Monitoring System**, using an existing SCADA/DMS system supplied in 2019. Feeders are circuits that carry electricity to groups of consumers. Connecting their monitoring systems is a different task from replacing each consumer’s meter.')
caption('Source D page 1 point 3. The 100 percent figure relates to feeder monitoring integration.')
image('smart_feeders',width=6.55,maxheight=3.05)
p('**Meaning.** The feeder monitoring claim does not establish completion of household smart meter installation or billing integration. Each milestone needs its own dated count and acceptance record.',size=9.8)

page('11 RDSS records match on works value but need a dated reconciliation')
p('The new note and the earlier project table both identify **Rs 106.54 crore of RDSS network or loss reduction works**. The new note also gives an approved project report estimate of **Rs 83.14 crore** and a central grant sanction of **Rs 49.88 crore**. The award value is **Rs 23.40 crore above the estimate**; the pages do not explain the difference in scope or cost.')
p('For 2025–26 the new note reports **Rs 46.45 crore incurred**, comprising **Rs 13.57 crore from grant funds plus Rs 32.88 crore from the state share**. Those two amounts reconcile exactly. Its 60 percent central funding statement relates to the approved project report cost, rather than the higher works award value.',size=10)
caption('Source D page 2 RDSS loss reduction works. The estimate grant award progress and expenditure figures are highlighted.')
image('rdss_funding',width=6.7,maxheight=3.6)
table(['Measure','Earlier project reply\nSource B','New project note\nSource D'],[
 ['Works value','Rs 106.54 crore','Rs 106.54 crore'],
 ['Materials supplied','80 percent','Around 75 percent'],
 ['Installation completed','37 percent','20 percent'],
 ['2025–26 financial figure','Rs 47 crore\nReleased or expended','Rs 46.45 crore\nIncurred']],widths=[2.3,2.2,2.2])
caption('Source B page 4 project 4. Original progress and financial column headings are retained for comparison with Source D above.')
image('rdss',width=6.7,maxheight=1.6)
p('**Meaning.** The matching works value links the two records, but their progress figures use unconfirmed matching dates and their financial columns use different descriptions. They cannot establish a rise or fall in progress or a missing funds amount without a dated reconciliation.',size=9.8)
p('The Rs 383.59 crore smart meter award, Rs 106.54 crore network works value, Rs 49.88 crore sanctioned grant and annual expenditure describe different items. Keeping them separate prevents double counting and unsupported loss claims.',size=9.5)
'''
s=s.replace("OUT.parent.mkdir(parents=True,exist_ok=True)",new+"\nOUT.parent.mkdir(parents=True,exist_ok=True)")
p.write_text(s)
print('Report builder updated with Findings 9 to 11 and Source D')
