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

public class BinarySearchTree {
    private TreeNode root = null;

    BinarySearchTree() {
    }

    /**
     * Tell's the root node to insert a value. If root node is not present, the creates it
     * @param value The value to inserted in the tree
     */
    public void insert(int value) {
        if (root == null)
            root = new TreeNode(value);
        else
            root = root.insert(value);
    }

    public void positionNodes(int width) {
        if (root != null)
            root.positionSelf(0, width, 0);
    }

    public void draw(Canvas c) {
        root.draw(c);
    }

    public int click(float x, float y, int target) {
        return root.click(x, y, target);
    }

    /**
     * Searches to find if current value is in Tree or not
     * @param value The value to find
     * @return The node, if value is present else null
     */
    private TreeNode search(int value) {
        TreeNode current = root;

        while (current != null) {
            if (current.getValue() == value)
                break;
            else if (current.getValue() > value)
                current = current.left;
            else
                current = current.right;
        }

        return current;
    }

    public void invalidateNode(int targetValue) {
        TreeNode target = search(targetValue);
        if (target != null)
            target.invalidate();
    }
}
