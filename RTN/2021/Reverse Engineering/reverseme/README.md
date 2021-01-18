**reverseme**
==========
**Tools used:** `DnSpy and C#`\
**Flag:** `RTN{1tty_B1tty_B1t_sh1ft5}`\
**Challenge Points:** `200`\
**Challenge Message:**
```
So you think you are a reverser huh? Reverse this one for me and prove your worth!
```
**Let's get into it**
==========
This is a `.NET` Challenge so let's use `Dnspy` to decompile the challenge.

**Decompiled Code**
==========
```c#
		// Token: 0x06000001 RID: 1 RVA: 0x00002050 File Offset: 0x00000250
		private static void Main(string[] args)
		{
			Console.WriteLine("Welcome.");
			Console.WriteLine("Please enter the password to continue:");
			for (;;)
			{
				Console.WriteLine();
				Console.Write("> ");
				if (Program.AllThatMatters(Program.FairAndSquare(Console.ReadLine()), Program.TopSecretData()))
				{
					break;
				}
				Console.WriteLine("Nope!");
			}
			Console.WriteLine("Correct!");
		}

		// Token: 0x06000002 RID: 2 RVA: 0x000020AC File Offset: 0x000002AC
		private static byte[] FairAndSquare(string input)
		{
			byte[] bytes = Encoding.ASCII.GetBytes(input);
			byte[] array = new byte[bytes.Length];
			for (int i = 0; i < bytes.Length; i++)
			{
				array[array.Length - 1 - i] = Program.QualityContent(bytes[i]);
			}
			return array;
		}

		// Token: 0x06000003 RID: 3 RVA: 0x000020F0 File Offset: 0x000002F0
		private static byte QualityContent(byte b1)
		{
			byte b2 = 0;
			for (int i = 0; i < 8; i++)
			{
				int num = b1 >> i & 1;
				b2 |= (byte)(num << 7 - i);
			}
			return b2;
		}

		// Token: 0x06000004 RID: 4 RVA: 0x00002124 File Offset: 0x00000324
		private static bool AllThatMatters(byte[] a, byte[] b)
		{
			if (a.Length != b.Length)
			{
				return false;
			}
			for (int i = 0; i < a.Length; i++)
			{
				if (a[i] != b[i])
				{
					return false;
				}
			}
			return true;
		}

		// Token: 0x06000005 RID: 5 RVA: 0x00002154 File Offset: 0x00000354
		private static byte[] TopSecretData()
		{
			return new byte[]
			{
				190,
				172,
				46,
				102,
				140,
				22,
				206,
				250,
				46,
				140,
				66,
				250,
				158,
				46,
				46,
				140,
				66,
				250,
				158,
				46,
				46,
				140,
				222,
				114,
				42,
				74
			};
		}
```

Alright this is easy let's just edit `FairAndSquare` function to accept bytes.

```c#
		private static byte[] FairAndSquare(byte[] bytes)
		{
			byte[] array = new byte[bytes.Length];
			for (int i = 0; i < bytes.Length; i++)
				array[array.Length - 1 - i] = Program.QualityContent(bytes[i]);
			return array;
		}
```

and then use it like this

```c#
Console.WriteLine(string.Join("", FairAndSquare(TopSecretData()).Select(chr => (char)chr)));
```

After running it we will get the flag, which is `RTN{1tty_B1tty_B1t_sh1ft5}`