"""
Deoxyribonucleic acid (DNA) is a chemical found in the nucleus of cells and
carries the "instructions" for the development and functioning
of living organisms.

If you want to know more http://en.wikipedia.org/wiki/DNA

In DNA strings, symbols "A" and "T" are complements of each other,
as "C" and "G". You have function with one side of the DNA
(string, except for Haskell); you need to get the other complementary side.
DNA strand is never empty or there is no DNA at all (again, except for Haskell).
"""
public class DnaStrand {
  public static String makeComplement(String dna) {
    String complement = new String("");
    for (int i =0; i< dna.length(); i++) {
        switch (dna.charAt(i)) {
          case 'A': complement+= 'T';
                    break;
          case 'T': complement+= 'A';
                    break;

          case 'G': complement+= 'C';
                    break;
          case 'C': complement+= 'G';
                    break;
        }
    }
  return complement;
  }
}
