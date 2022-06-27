/*
 Navicat SQLite Data Transfer

 Source Server         : software
 Source Server Type    : SQLite
 Source Server Version : 3035005
 Source Schema         : main

 Target Server Type    : SQLite
 Target Server Version : 3035005
 File Encoding         : 65001

 Date: 26/06/2022 13:14:26
*/

PRAGMA foreign_keys = false;

-- ----------------------------
-- Table structure for nameAndPassword
-- ----------------------------
DROP TABLE IF EXISTS "nameAndPassword";
CREATE TABLE "nameAndPassword" (
  "name" text NOT NULL,
  "password" text NOT NULL,
  PRIMARY KEY ("name")
);

-- ----------------------------
-- Table structure for record
-- ----------------------------
DROP TABLE IF EXISTS "record";
CREATE TABLE "record" (
  "name" text NOT NULL,
  "year" text NOT NULL,
  "month" text NOT NULL,
  "day" text NOT NULL,
  "types" text,
  "usage" text,
  "more" text,
  "number" real NOT NULL,
  PRIMARY KEY ("name")
);

PRAGMA foreign_keys = true;
