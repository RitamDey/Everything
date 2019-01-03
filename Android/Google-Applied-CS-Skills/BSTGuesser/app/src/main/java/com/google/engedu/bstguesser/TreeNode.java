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

    TreeNode(int value) {
        this.value = value;
        this.height = 1;
        this.showValue = true;
        this.left = null;
        this.right = null;
    }

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

        this.height = 1 + Math.max(this.getHeight(this.left), this.getHeight(this.right));

        int balance = this.getBalance();

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

        return this;
    }

    public int getValue() {
        return value;
    }

    public int getHeight(TreeNode node) {
        if (node == null)
            return 0;
        return node.height;
    }

    private TreeNode leftRotate(TreeNode node) {
        if (node == null)
            return null;

        TreeNode rightChild = node.right;
        node.right = rightChild.left;
        rightChild.left = node;

        node.height = Math.max(this.getHeight(node.left), this.getHeight(node.right)) + 1;
        rightChild.height = Math.max(this.getHeight(rightChild.right), this.getHeight(rightChild.left)) + 1;

        return rightChild;
    }

    private TreeNode rightRotate(TreeNode node) {
        if (node == null)
            return null;

        TreeNode leftChild = node.left;
        node.left = leftChild.right;
        leftChild.right = node;

        node.height = Math.max(this.getHeight(node.left), this.getHeight(node.right)) + 1;
        leftChild.height = Math.max(this.getHeight(leftChild.right), this.getHeight(leftChild.left)) + 1;

        return leftChild;
    }

    private int getBalance() {
        // Get the height of left subtree and right subtree
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

    public void invalidate() {
        color = Color.CYAN;
        showValue = true;
    }
}
