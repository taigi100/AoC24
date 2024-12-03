package.path = "./luajit/share/lua/5.1/?.lua;" .. package.path
package.cpath = "./luajit/lib/lua/5.1/?.so;" .. package.cpath

local inspect = require("inspect")
local M = require("moses")

M.
function split(str, sep)
	if sep == nil then
		sep = "%s"
	end
	local t = {}
	for s in string.gmatch(str, "([^" .. sep .. "]+)") do
		table.insert(t, s)
	end
	return t
end

local function read_input(filename)
	local file = io.open(filename, "r")
	if not file then
		return nil
	end
	local content = file:read("*all")
	file:close()
	return content
end

-- Read input
-- Part 1 solution
local function solve_part1()
	return "Not Implemented"
end

-- Part 2 solution
local function solve_part2()
	return "Not Implemented"
end

-- Solve and print results
print("Part 1:", solve_part1())
print("Part 2:", solve_part2())
