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

package com.google.engedu.touringmusician;


import android.graphics.Point;
import android.support.annotation.NonNull;
import android.util.Log;

import java.util.Iterator;

public class CircularLinkedList implements Iterable<Point> {

    private class Node {
        Point point;
        Node prev, next;

        Node(Point p) {
            this.point = p;
            this.prev = null;
            this.next = null;
        }
    }

    Node head = null;

    public void insertBeginning(Point p) {
        Node point = new Node(p);

        if (this.head == null) {
            this.head = point;
            this.head.next = this.head;
            this.head.prev = this.head;
        }
        else {
            point.next = this.head;
            point.prev = this.head.prev;
            this.head.prev.next = point;
            this.head.prev = point;
            this.head = point;
        }
    }

    private float distanceBetween(Point from, Point to) {
        return (float) Math.sqrt(Math.pow(from.y - to.y, 2) + Math.pow(from.x - to.x, 2));
    }

    public float totalDistance() {
        float total = 0;
        Point prev = null;

        for (Point elem: this) {
            if (prev != null)
                total += this.distanceBetween(prev, elem);

            prev = elem;
        }

        if (prev != null) {
            total += this.distanceBetween(prev, this.head.point);
        }

        return total;
    }

    public void insertNearest(Point p) {
        Node point = new Node(p);

        if (this.head == null) {
            point.next = point;
            point.prev = point;
            this.head = point;
            return;
        }

        float currDistance = Float.MAX_VALUE;
        Node currPoint = this.head;
        Node curr = this.head.next;
        float dist;

        while (curr != this.head) {
            dist = this.distanceBetween(curr.point, p);

            if (dist <= currDistance) {
                currPoint = curr;
                currDistance = dist;
            }
            curr = curr.next;
        }

        point.next = currPoint.next;
        point.prev = currPoint;
        currPoint.next.prev = point;
        currPoint.next = point;
    }

    public void insertSmallest(Point p) {
        /**
         **
         **  YOUR CODE GOES HERE
         **
         **/
    }

    public void reset() {
        head = null;
    }

    private class CircularLinkedListIterator implements Iterator<Point> {

        Node current;

        public CircularLinkedListIterator() {
            current = head;
        }

        @Override
        public boolean hasNext() {
            return (current != null);
        }

        @Override
        public Point next() {
            Point toReturn = current.point;
            current = current.next;
            if (current == head) {
                current = null;
            }
            return toReturn;
        }

        @Override
        public void remove() {
            throw new UnsupportedOperationException();
        }
    }

    @NonNull
    @Override
    public Iterator<Point> iterator() {
        return new CircularLinkedListIterator();
    }


}
