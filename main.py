from hf import generate_response
import time
def tempreture_prompt_activity():
    print("="*70)
    print("ADVANCED PROMPT ENGENIRING:TEMPRETUER+INSTROCTIONS")
    print("="*70)
    print("/n PART 1:TEMPRATURE EXPLORATION")
    base= input("   Enter a creative prompt :").strip():
    for t,label in [(0.1,"LOW(O.1)"-Deterministic)
                    (0.5,"MEDIUM(O.5)"-Balanced)
                    (0.9,"HIGH(O.9)"-Creative)]
                print(f"/n---{label}---")
                print("generate_response(base,temprature=t,max_tokens=512 )")
                time.sleep(1)
                print(/nPart2 : INSTRUCTION BASE)