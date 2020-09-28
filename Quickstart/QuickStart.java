import javax.swing.*;
// public class QuickStart {
//     public static void main(String[] args) {
//         System.out.println("Hello, World.");
//     }
// }

class gui{
    public static void main(String args[]){
       JFrame frame = new JFrame("DeployResource");
       frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
       frame.setSize(1100,850);
       JRadioButton configurenr = new JRadioButton("Configure New Resource");
       configurenr.setBounds(75,50,100,30);
       JRadioButton selecter = new JRadioButton("Select Existing Resource");
       selecter.setBounds(75,100,100,30); 
       frame.getContentPane().add(configurenr); // Adds Button to content pane of frame
       frame.getContentPane().add(selecter); // Adds Button to content pane of frame
       frame.setVisible(true);

    }
}