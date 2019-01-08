/* Copyright 2016 Google Inc.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package com.google.engedu.bstguesser;

import android.graphics.Canvas;
import android.graphics.Color;
import android.graphics.Paint;

public class TreeNode {
    private static final int SIZE = 60;
    private static final int MARGIN = 20;
    private int value, height;
    protected TreeNode left, right;
    private boolean showValue;
    private int x, y;
    private int color = Color.rgb(150, 150, 250);

    /**
     * Constructor for the class
     * @param value The value of the node in the Tree
     */
    TreeNode(int value) {
        this.value = value;
        this.height = 1;
        this.showValue = false;
        this.left = null;
        this.right = null;
    }

    /**
     * Inserts the value in the tree
     * @param valueToInsert The value that needs to be inserted in the tree
     * @return The current node or new rebalanced node
     */
    public TreeNode insert(int valueToInsert) {
        if (this.value > valueToInsert) {
            if (this.left != null)
                this.left = this.left.insert(valueToInsert);
            else
                this.left = new TreeNode(valueToInsert);
        }
        else if (this.value < valueToInsert) {
            if (this.right != null)
                this.right = this.right.insert(valueToInsert);
            else
                this.right = new TreeNode(valueToInsert);
        }

        // Update the height of the current node using the heights of its children
        this.height = 1 + Math.max(this.getHeight(this.left), this.getHeight(this.right));

        // Get balanced factor to see if we need re-balancing
        int balance = this.getBalance();

        /*
         * There are only 4 types of rotations that can be done.
         * Left Left Rotation -> Perform a single right rotation on the unbalanced node.
         * Left Right Rotation -> Perform a left rotation on the unbalanced node's left child, the perform a right rotation on itself
         * Right Right Rotation -> Perform a single left rotation on the unbalanced node.
         * Right Left Rotation -> Perform a right rotation on the unbalanced node's right child, the perform a left rotation on itself
         */

        /* Identify cases for rotations/balancing.
         *
         * Left Left Case -> When balance factor > 1 and inserted value < left child's value
         * Left Right Case -> When balance factor > 1 and inserted value > left child's value
         *
         * Right Right Case -> When balance factor < 1 and inserted value > right child's value
         * Right Left Case -> When balanced factor < 1 and inserted value < right child's value
         */
        if (balance > 1) {
            if (valueToInsert < this.left.value)
                return this.rightRotate(this);
            else if (valueToInsert > this.left.value) {
                this.left = this.leftRotate(this.left);
                return this.rightRotate(this);
            }
        } else if (balance < -1) {
            if (valueToInsert > this.right.value)
                return this.leftRotate(this);
            else if (valueToInsert < this.right.value) {
                this.right = this.rightRotate(this.right);
                return this.leftRotate(this);
            }
        }

        // If we reached here, then it means we did a regular BST insertion, return the current node
        return this;
    }

    public int getValue() {
        return value;
    }

    /**
     * Helper method that returns a node's height
     * @param node A node whose height needs to be returned
     * @return The node's height
     */
    private int getHeight(TreeNode node) {
        if (node == null)
            return 0;
        return node.height;
    }

    /**
     * Performs a left rotation on the given node
     * @param node The root to the current unbalanced subtree
     * @return The root of the subtree after performing the left rotation
     */
    private TreeNode leftRotate(TreeNode node) {
        if (node == null)
            return null;

        TreeNode rightChild = node.right;
        node.right = rightChild.left;
        rightChild.left = node;

        // Since only the position of the nodes changed in the tree,
        // the unmoved child nodes have their heights unchanged. Use them to recalculate the heights
        node.height = Math.max(this.getHeight(node.left), this.getHeight(node.right)) + 1;
        rightChild.height = Math.max(this.getHeight(rightChild.right), this.getHeight(rightChild.left)) + 1;

        return rightChild;
    }

    /**
     * Performs a right rotation on the given node
     * @param node The root to the current unbalanced subtree
     * @return The root of the subtree after performing the right rotation
     */
    private TreeNode rightRotate(TreeNode node) {
        if (node == null)
            return null;

        TreeNode leftChild = node.left;
        node.left = leftChild.right;
        leftChild.right = node;

        // Since only the position of the nodes changed in the tree,
        // the unmoved child nodes have their heights unchanged. Use them to recalculate the heights
        node.height = Math.max(this.getHeight(node.left), this.getHeight(node.right)) + 1;
        leftChild.height = Math.max(this.getHeight(leftChild.right), this.getHeight(leftChild.left)) + 1;

        return leftChild;
    }

    /**
     * Calculates the current balance between left and right subtree
     * @return The current balance of the node
     */
    private int getBalance() {
        int left = (this.left != null)? this.left.height: 0;
        int right = (this.right != null)? this.right.height: 0;

        return left - right;
    }

    public void positionSelf(int x0, int x1, int y) {
        this.y = y;
        x = (x0 + x1) / 2;

        if(left != null) {
            left.positionSelf(x0, right == null ? x1 - 2 * MARGIN : x, y + SIZE + MARGIN);
        }
        if (right != null) {
            right.positionSelf(left == null ? x0 + 2 * MARGIN : x, x1, y + SIZE + MARGIN);
        }
    }

    public void draw(Canvas c) {
        Paint linePaint = new Paint();
        linePaint.setStyle(Paint.Style.STROKE);
        linePaint.setStrokeWidth(3);
        linePaint.setColor(Color.GRAY);
        if (left != null)
            c.drawLine(x, y + SIZE/2, left.x, left.y + SIZE/2, linePaint);
        if (right != null)
            c.drawLine(x, y + SIZE/2, right.x, right.y + SIZE/2, linePaint);

        Paint fillPaint = new Paint();
        fillPaint.setStyle(Paint.Style.FILL);
        fillPaint.setColor(color);
        c.drawRect(x-SIZE/2, y, x+SIZE/2, y+SIZE, fillPaint);

        Paint paint = new Paint();
        paint.setColor(Color.BLACK);
        paint.setTextSize(SIZE * 2/3);
        paint.setTextAlign(Paint.Align.CENTER);
        c.drawText(showValue ? String.valueOf(value) : "?", x, y + SIZE * 3/4, paint);

        if (height > 0) {
            Paint heightPaint = new Paint();
            heightPaint.setColor(Color.MAGENTA);
            heightPaint.setTextSize(SIZE * 2 / 3);
            heightPaint.setTextAlign(Paint.Align.LEFT);
            c.drawText(String.valueOf(height), x + SIZE / 2 + 10, y + SIZE * 3 / 4, heightPaint);
        }

        if (left != null)
            left.draw(c);
        if (right != null)
            right.draw(c);
    }

    public int click(float clickX, float clickY, int target) {
        int hit = -1;
        if (Math.abs(x - clickX) <= (SIZE / 2) && y <= clickY && clickY <= y + SIZE) {
            if (!showValue) {
                if (target != value) {
                    color = Color.RED;
                } else {
                    color = Color.GREEN;
                }
            }
            showValue = true;
            hit = value;
        }
        if (left != null && hit == -1)
            hit = left.click(clickX, clickY, target);
        if (right != null && hit == -1)
            hit = right.click(clickX, clickY, target);
        return hit;
    }

    /**
     * As per as I understood reading the sourcecode, this method forces activity redraw
     */
    public void invalidate() {
        color = Color.CYAN;
        showValue = true;
    }
}
