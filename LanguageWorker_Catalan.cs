// Assembly-CSharp, Version=1.5.8874.2866, Culture=neutral, PublicKeyToken=null
// Verse.LanguageWorker_Catalan
using Verse;

public class LanguageWorker_Catalan : LanguageWorker
{
	public override string WithIndefiniteArticle(string str, Gender gender, bool plural = false, bool name = false)
	{
		if( str.NullOrEmpty() )
			return str;

		if( name )
			return WithElLaArticle(str, gender, true);
		else if( plural )
			return (gender == Gender.Female ? "unes " : "uns ") + str;
		else
			return (gender == Gender.Female ? "una " : "un ") + str;
	}

	public override string WithDefiniteArticle(string str, Gender gender, bool plural = false, bool name = false)
	{
		if( str.NullOrEmpty() )
			return str;

		if( name )
			return WithElLaArticle(str, gender, true);
		else if( plural )
			return (gender == Gender.Female ? "les " : "els ") + str;
		else
			return WithElLaArticle(str, gender, false);
	}

	private string WithElLaArticle(string str, Gender gender, bool name)
	{
		if( str.Length != 0 && (IsVowel(str[0]) || str[0] == ’h’ || str[0] == ’H’) )
		{
			if( name && gender == Gender.Male)
				return "n’" + str;
			else
				return "l’" + str;
		}
		else
			return (gender == Gender.Female ? "la " : "el ") + str;
	}

	public override string OrdinalNumber(int number, Gender gender = Gender.None)
	{
		if ( gender == Gender.none) return number;

		if( gender == Gender.Female )
			return number + "a";

        switch ( number )
        {
        case 1:  return number + "r"; // Primer
        case 2:  return number + "n"; // Segon
        case 3:  return number + "r"; // Tercer
        case 4:  return number + "t"; // Quart
        default: return number + "è"; // Cinquè i posteriors
        }
	}

	public override string Pluralize(string str, Gender gender, int count = -1)
	{
		if (str.NullOrEmpty())
		{
			return str;
		}
		if (TryLookupPluralForm(str, gender, out var plural, count))
		{
			return plural;
		}
		if (count != -1 && count < 2)
		{
			return str;
		}

		string lowercase = str.ToLowerDynamic();
		
		// 1. Paraules acabades en -a canvien a -es (vocal canviant)
		if (lowercase.EndsWith("a"))
		{
			// Gestió de canvis ortogràfics respiratoris/fonètics comuns
			if (lowercase.EndsWith("ca")) return str.Substring(0, str.Length - 2) + "ques";
			if (lowercase.EndsWith("ga")) return str.Substring(0, str.Length - 2) + "gues";
			if (lowercase.EndsWith("ja")) return str.Substring(0, str.Length - 2) + "ges";
			if (lowercase.EndsWith("ça")) return str.Substring(0, str.Length - 2) + "ces";
			if (lowercase.EndsWith("qua")) return str.Substring(0, str.Length - 3) + "qües";
			if (lowercase.EndsWith("gua")) return str.Substring(0, str.Length - 3) + "gües";
			
			return str.Substring(0, str.Length - 1) + "es";
		}
		
		// 2. Paraules agudes acabades en vocal tònica afegeixen -ns
		if (lowercase.EndsWith("à") || lowercase.EndsWith("é") || lowercase.EndsWith("è") || 
			lowercase.EndsWith("í") || lowercase.EndsWith("ó") || lowercase.EndsWith("ò") || lowercase.EndsWith("ú"))
		{
			// Es treu l’accent al pluralitzar amb -ns
			string senseAccent = TreureAccentFinal(str);
			return senseAccent + "ns";
		}
		
		// 3. Paraules acabades en -s, -ç, -x, -tx (afegeixen -os si són agudes)
		if (lowercase.EndsWith("s") || lowercase.EndsWith("ç") || lowercase.EndsWith("x") || lowercase.EndsWith("tx"))
		{
			// Nota: RimWorld sol assumir que els noms d’objectes/animals curts en -s fan el plural en -os (gos -> gossos)
			if (lowercase.EndsWith("s") && !lowercase.EndsWith("as") && !lowercase.EndsWith("es") && !lowercase.EndsWith("is") && !lowercase.EndsWith("os") && !lowercase.EndsWith("us"))
			{
				return str + "os"; // Ex: nas -> nasos
			}
			return str + "os";
		}
		
		// 4. Cas general: afegeix -s (vocals àtones i la majoria de consonants)
		return str + "s";
	}
	
	private static string TreureAccentFinal(string paraula)
	{
		if (paraula.EndsWith("à")) return paraula.Substring(0, paraula.Length - 1) + "a";
		if (paraula.EndsWith("é") || paraula.EndsWith("è")) return paraula.Substring(0, paraula.Length - 1) + "e";
		if (paraula.EndsWith("í")) return paraula.Substring(0, paraula.Length - 1) + "i";
		if (paraula.EndsWith("ó") || paraula.EndsWith("ò")) return paraula.Substring(0, paraula.Length - 1) + "o";
		if (paraula.EndsWith("ú")) return paraula.Substring(0, paraula.Length - 1) + "u";
		return paraula;
	}

	public bool IsVowel(char ch)
	{
		return "aeiouAEIOUàèéíòóúÀÈÉÍÒÓÚïüÏÜ".IndexOf(ch) >= 0;
	}

	public override string PostProcessed(string str)
	{
		return PostProcessedInt(base.PostProcessed(str));
	}

	public override string PostProcessedKeyedTranslation(string translation)
	{
		return PostProcessedInt(base.PostProcessedKeyedTranslation(translation));
	}

	private string PostProcessedInt(string str)
	{
		return str.Replace(" de el ", " del ")
			.Replace(" de els ", " dels ")
			.Replace(" a el ", " al ")
			.Replace(" a els ", " als ")
			.Replace(" per el ", " pels ")
			.Replace(" per els ", " pels ");
			//.Replace("’", "’"); This would be great, but nicknames use ’this approach’.
	}
}
