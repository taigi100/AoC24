local inspect = require("inspect")
local M = require("moses")

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

-- Read input
local left = {}
local right = {}

for line in io.lines("in.txt") do
	local tmp = split(line, " ")
	if tmp[1] then
		table.insert(left, tmp[1])
		table.insert(right, tmp[2])
	end
end

-- Part 1 solution
local function solve_part1()
	local distance = 0
	local temp_left = M.clone(left)
	local temp_right = M.clone(right)
	table.sort(temp_left)
	table.sort(temp_right)
	for i = 1, #temp_left do
		distance = distance + math.abs(temp_left[i] - temp_right[i])
	end

	return distance
end

-- Part 2 solution
local function solve_part2()
	local right_dict = {}
	for i = 1, #right do
		local val = right[i]
		right_dict[val] = (right_dict[val] or 0) + 1
	end
	local ans = 0
	for i = 1, #left do
		local val = left[i]
		if right_dict[val] then
			ans = ans + (val * right_dict[val])
		end
	end

	return ans
end

-- Solve and print results
print("Part 1:", solve_part1())
print("Part 2:", solve_part2())
