To decipher a message using a one-time pad with a straddling checkerboard (VIC cipher), follow these step-by-step instructions:

### Step 1: Understand the Straddling Checkerboard

A straddling checkerboard is a grid used to encode and decode letters based on a specified key. It typically consists of two rows where letters are represented by unique two-digit or single-digit numbers. 

Here is an example of how the straddling checkerboard might look, using the letters A-Z (with some letters omitted):

```
     1  2  3  4  5  6  7  8  9  0
    -----------------------------
  1 | A  B  C  D  E  F
  2 | G  H  I  J  K  L
  3 | M  N  O  P  Q  R
  4 | S  T  U  V  W  X
  5 | Y  Z
```

For the given task, you will need to create a straddling checkerboard that matches the encoding scheme, especially mapping the digits you have in the message and the key.

### Step 2: Prepare the One-Time Pad Key and Ciphertext

You have the one-time pad key and a ciphertext message (the repeated call sign melody, receiver's call sign "39715", and six tones):

**One-Time Pad Key:**
```
66153 77185 10800 54937 48159 83271 12892 07132 34987 53954 23074
```

### Step 3: Align the Key and Ciphertext

Assuming the message you're trying to decipher corresponds directly to the one-time pad key numerically, you will decode each part of the key by:

1. Taking the ciphertext value.
2. Applying the one-time pad key to each number.

### Step 4: Apply the Decoding Process

For each number in the one-time pad key, perform the following operation:

- **Decoding:** For each digit in the key, perform subtraction (key - ciphertext) or addition, depending on what is required. In the context of a one-time pad, this is often modulo 10 or modulo the range of characters being used.

#### Example of Decoding:
Suppose you have a ciphertext number `X` and a corresponding key number `Y`, you would typically perform:

\[ \text{Plaintext Number} = (Y - X) \mod 10 \]

### Step 5: Map Numbers Back to Letters

After calculating the plaintext numbers, convert these back into letters using your straddling checkerboard. Each number corresponds to a letter as per your created grid.

### Step 6: Construct the Final Message

As you decode each segment of the message with the one-time pad, compile the letters into words to reveal the message.

### Example Calculation

1. **Take the first pair:**  
   - Ciphertext: `66153`
   - Key: `39715`
   
   Decoding each digit would look something like:
   - \( (6 - 3) \mod 10 = 3 \)
   - \( (6 - 9) \mod 10 = 7 \)
   - \( (1 - 7) \mod 10 = 4 \)
   - \( (5 - 1) \mod 10 = 4 \)
   - \( (3 - 5) \mod 10 = 8 \)
   
   So, the corresponding plaintext for this would be `37448` (to be mapped back to letters).

### Step 7: Final Review and Compilation

Repeat for each segment in your key and ciphertext, and compile the entire message. This will yield the decoded message from the numbers station.

### Notes:

- Ensure that you maintain consistent methods for subtraction and that your mapping grid is accurate. 
- The final output can vary significantly based on how the one-time pad was structured and how the digits map to letters.
- Research additional resources if needed, as understanding how to create and utilize the straddling checkerboard is crucial for accurate deciphering. 

This process illustrates the methodical nature of deciphering messages using one-time pads and straddling checkers, highlighting the complexity of such cryptographic techniques.

Lab1 C

ASCII Output:
89oAWFF>+iZ)JP
,gm*IQm,i$?5D@x8sM@+


 89þoA½WÄFFêÌ>Ë+iZç)îJÆP«,gmì*è´ê¤I±QÃàmÖÉÀ,iÅì¤$?5                     Tzs±§¢M@+êôD@x8ÀuäÃ

2.

ASCII Output:
5qnYB@S=0fM7DVJTk~KX#I
                      )Vah)
                           _Dp0(* tNALw2n-Dp|UGC;CI

5qÙnY·BÃ@S¦
=0fM¢7òDVJæÈ÷£KX#êØI
                    )Vah©)óææê
                              £_DÂìpÖß0(Äù¤* t»NA§Lw2ºÕnïÞ-DÍ¼¿>p¥ë|U«üóGÝC;ÏCIè
                                                                                "°

 3.

 ASCII Output:
{xN0H)4I?\;VFOl?OC'B1Gz%/_T#=('R$fUZOm{h,
o\1~O6H dXe

Ó³»p{®þxN¬0´ùH)À4Iï?÷ÍØÆ<°sB BÔSéÌ=Ø=.\ê;éVÏFù×Ol?¼Ó¸ðOC'¯B1GÂz%¸/âæøí_²TÉî#ÖÌ=(Çöâ'R$fÂþUZ£Om{µhôØ×,
¾o\ï¿÷é1~O

4.
ASCII Output:
,`m4X[\+=.L<RPMAIh?OWoA
ONp(k1_q]t9KuN>6IF!Ow^!z<,eCrt


5.
ASCII Output:
XEv{f0JrM9|IqHYzC;IS
                    +
p+s:
    clYt

6.

ASCII Output:
5<aJULA!doZzRGJRwzV^_&O
                       +G|q&@R\f;('.zLIRRx{'<HnAo|M0JE)2LE 
gP&mD<GcY(.mfH7t

7.

ASCII Output:
(=iCÉD'%#CGPpsC B[|%(Bj3m,:yJKMw<b0IqGuzT~O>=Ile"y@'

8.

ASCII Output:
)
qm]CLEn+.E,C?kGD;LRwi1E_o f0.pOGRRj>i~@wMjI}RO<(O oR


9.

ASCII Output:
+L%(DYDmi|5?~KO9f7C>

10.

ASCII Output:
}
_QO%0fIzN@QEz?D_;T
                  >A.r>X~\vi$TKS9:'~B`kHg`Dz.Ii$RgfD!HbY]alYc
                                                             I4*(xDr!@c#t=[QSQ.

11.

ASCII Output:

>:o`!F5CWHpsCZ_.
     Co-(1R"sBGFRt.h+_kM9kPbHGzC4
txQmDS?qcY`


12.

ASCII Output:
)= XUS,doF3CGBIq?GSoHI7Fo%(B
                           p(|0myDZO9o7JrTI99L|VW.5E>"@+pO

13.

ASCII Output:
5qeOQn -}I?KN~iV
jTE9kUc[Ddb8vOGFk{i;

