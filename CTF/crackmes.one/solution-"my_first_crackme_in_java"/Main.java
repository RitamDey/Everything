package defpackage;

import java.awt.EventQueue;
import java.awt.Font;
import java.awt.Rectangle;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.logging.Level;
import java.util.logging.Logger;
import javax.swing.BorderFactory;
import javax.swing.DefaultComboBoxModel;
import javax.swing.GroupLayout;
import javax.swing.GroupLayout.Alignment;
import javax.swing.JButton;
import javax.swing.JComboBox;
import javax.swing.JDialog;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JTextField;
import javax.swing.LayoutStyle.ComponentPlacement;
import javax.swing.UIManager;
import javax.swing.UIManager.LookAndFeelInfo;
import javax.swing.UnsupportedLookAndFeelException;

/* renamed from: Main */
public class Main extends JFrame {
    private JComboBox c1;
    private JButton clear;
    private JButton done;
    private JDialog jDialog1;
    private JLabel jLabel1;
    private JLabel jLabel2;
    private JLabel jLabel3;
    private JPanel jPanel1;
    private JTextField t1;
    private JTextField t2;

    /* renamed from: Main$1 */
    class DoneButtonListener implements ActionListener {
        DoneButtonListener() {
        }

        public void actionPerformed(ActionEvent evt) {
            Main.this.doneActionPerformed(evt);
        }
    }

    /* renamed from: Main$2 */
    class ClearButtonListener implements ActionListener {
        ClearButtonListener() {
        }

        public void actionPerformed(ActionEvent evt) {
            Main.this.clearActionPerformed(evt);
        }
    }

    /* renamed from: Main$3 */
    static class 3 implements Runnable {
        3() {
        }

        public void run() {
            new Main().setVisible(true);
        }
    }

    public Main() {
        initComponents();
    }

    private void initComponents() {
        this.jDialog1 = new JDialog();
        this.jPanel1 = new JPanel();
        this.jLabel1 = new JLabel();
        this.t1 = new JTextField();
        this.jLabel2 = new JLabel();
        this.t2 = new JTextField();
        this.jLabel3 = new JLabel();
        this.c1 = new JComboBox();
        this.done = new JButton();
        this.clear = new JButton();
        GroupLayout jDialog1Layout = new GroupLayout(this.jDialog1.getContentPane());
        this.jDialog1.getContentPane().setLayout(jDialog1Layout);
        jDialog1Layout.setHorizontalGroup(jDialog1Layout.createParallelGroup(Alignment.LEADING).addGap(0, 400, 32767));
        jDialog1Layout.setVerticalGroup(jDialog1Layout.createParallelGroup(Alignment.LEADING).addGap(0, 300, 32767));
        setDefaultCloseOperation(3);
        setTitle("Crackme01");
        setBounds(new Rectangle(400, 200, 0, 0));
        setResizable(false);
        this.jPanel1.setBorder(BorderFactory.createTitledBorder(null, "Details", 0, 2, new Font("Times New Roman", 0, 13)));
        this.jLabel1.setText("Enter Name:");
        this.jLabel2.setText("Enter Key:");
        this.jLabel3.setText("Your Country:");
        this.c1.setModel(new DefaultComboBoxModel(new String[]{"Australia", "Brazil", "Egypt", "Germany", "India", "Mexico", "Other"}));
        this.done.setText("Done");
        this.done.addActionListener(new DoneButtonListener());
        this.clear.setText("Clear");
        this.clear.addActionListener(new ClearButtonListerner());
        GroupLayout jPanel1Layout = new GroupLayout(this.jPanel1);
        this.jPanel1.setLayout(jPanel1Layout);
        
        jPanel1Layout.setHorizontalGroup(
            jPanel1Layout.createParallelGroup(Alignment.LEADING)
            .addGroup(
                jPanel1Layout.createSequentialGroup()
                .addGap(26, 26, 26)
                .addGroup(
                    jPanel1Layout.createParallelGroup(Alignment.LEADING)
                    .addComponent(this.jLabel2, -2, 71, -2)
                    .addGroup(
                        jPanel1Layout.createSequentialGroup()
                        .addGroup(
                            jPanel1Layout.createParallelGroup(Alignment.LEADING)
                            .addComponent(this.jLabel1)
                            .addComponent(this.t1, -2, 149, -2)
                            .addComponent(this.t2, -2, 149, -2)
                        )
                        .addGap(33, 33, 33)
                        .addGroup(
                            jPanel1Layout.createParallelGroup(Alignment.LEADING, false)
                            .addComponent(this.jLabel3)
                            .addGroup(
                                jPanel1Layout.createSequentialGroup()
                                .addComponent(this.done, -2, 61, -2)
                                .addPreferredGap(ComponentPlacement.RELATED)
                                .addComponent(this.clear, -2, 61, -2)
                            )
                            .addComponent(this.c1, 0, -1, 32767)
                        )
                    )
                )
                .addContainerGap(30, 32767)
            ));

        jPanel1Layout.setVerticalGroup(
            jPanel1Layout.createParallelGroup(Alignment.LEADING)
            .addGroup(
                jPanel1Layout.createSequentialGroup()
                .addContainerGap()
                .addGroup(jPanel1Layout.createParallelGroup(Alignment.BASELINE)
                .addComponent(this.jLabel1)
                .addComponent(this.jLabel3))
                .addPreferredGap(ComponentPlacement.RELATED)
                .addGroup(jPanel1Layout.createParallelGroup(Alignment.BASELINE)
                .addComponent(this.t1, -2, -1, -2)
                .addComponent(this.c1, -2, -1, -2))
                .addPreferredGap(ComponentPlacement.UNRELATED)
                .addComponent(this.jLabel2)
                .addPreferredGap(ComponentPlacement.RELATED)
                .addGroup(
                    jPanel1Layout.createParallelGroup(Alignment.BASELINE)
                    .addComponent(this.t2, -2, -1, -2)
                    .addComponent(this.done)
                    .addComponent(this.clear)
                )
                .addContainerGap(36, 32767)
            )
        );


        GroupLayout layout = new GroupLayout(getContentPane());
        getContentPane().setLayout(layout);
        layout.setHorizontalGroup(
            layout.createParallelGroup(Alignment.LEADING)
            .addGroup(
                layout.createSequentialGroup()
                .addContainerGap()
                .addComponent(this.jPanel1, -2, -1, -2)
                .addContainerGap(-1, 32767)
            )
        );
        
        layout.setVerticalGroup(
            layout.createParallelGroup(Alignment.LEADING)
            .addGroup(
                layout.createSequentialGroup()
                .addContainerGap()
                .addComponent(this.jPanel1, -2, -1, -2)
                .addContainerGap(-1, 32767)
            )
        );

        pack();
    }

    private void doneActionPerformed(ActionEvent evt) {
        String selectedMenuOption = null;
        int nameInputSum = 0;
        String keyInput = this.t2.getText();
        String nameInput = this.t1.getText();
        Object selectedItem = this.c1.getSelectedItem();
        if (selectedItem != null) {
            selectedMenuOption = selectedItem.toString();
        }
        for (int i = 0; i < nameInput.length(); i++) {
            if (Character.isLetter(nameInput.charAt(i))) {
                nameInputSum += nameInput.charAt(i);
            }
        }
        if (Boolean.valueOf(new Dark().StrM(selectedMenuOption, keyInput, nameInputSum)).booleanValue()) {
            JOptionPane.showMessageDialog(this, "Successfully CrAcked", "Success", 1);
        } else {
            JOptionPane.showMessageDialog(this, "Invalid Key", "Error", 0);
        }
    }

    private void clearActionPerformed(ActionEvent evt) {
        this.t1.setText("");
        this.t2.setText("");
    }

    public static void main(String[] args) {
        try {
            for (LookAndFeelInfo info : UIManager.getInstalledLookAndFeels()) {
                if ("Nimbus".equals(info.getName())) {
                    UIManager.setLookAndFeel(info.getClassName());
                    break;
                }
            }
        } catch (ClassNotFoundException ex) {
            Logger.getLogger(Main.class.getName()).log(Level.SEVERE, null, ex);
        } catch (InstantiationException ex2) {
            Logger.getLogger(Main.class.getName()).log(Level.SEVERE, null, ex2);
        } catch (IllegalAccessException ex3) {
            Logger.getLogger(Main.class.getName()).log(Level.SEVERE, null, ex3);
        } catch (UnsupportedLookAndFeelException ex4) {
            Logger.getLogger(Main.class.getName()).log(Level.SEVERE, null, ex4);
        }
        EventQueue.invokeLater(new 3());
    }
}
