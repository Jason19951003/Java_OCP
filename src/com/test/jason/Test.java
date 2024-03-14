package com.test.jason;

public class Test {

	public static void main(String[] args) {
		try {
			int guess = Integer.parseInt(args[0]);
			if (guess < 1 || guess > 5) {
				System.out.println("程式用法 java GuessingGame [數字1-5]");
			} else {
				int random = (int) (Math.random() * 5) + 1;

				if (random == guess)
					System.out.println("恭喜猜對了!");
				else
					System.out.println("猜錯了,答案是" + random);
			}
		} catch (Exception e) {
			if (args[0].equals("help"))
				System.out.println("程式用法 java GuessingGame [數字1-5]");
			else
				System.out.println("輸入內容須為正整數");
		}
	}
}
