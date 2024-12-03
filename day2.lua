local inspect = require("inspect")
local moses = require("moses.lua")

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

local function sign(num)
	if num < 0 then
		return -1
	else
		return 1
	end
end

-- Read input
-- Part 1 solution
local function solve_part1()
	local safe = 0
	for line in io.lines("in.txt") do
		local nums = split(line, " ")
		local dir = sign(nums[2] - nums[1])
		local is_valid = 1
		for i = 2, #nums do
			if sign(nums[i] - nums[i - 1]) ~= dir or math.abs(nums[i] - nums[i - 1]) > 3 or nums[i] == nums[i - 1] then
				is_valid = 0
			end
		end
		safe = safe + is_valid
	end
	return safe
end

local function is_safe(arr)
	local dir = sign(arr[2] - arr[1])
	local is_valid = 1
	for i = 2, #arr do
		if sign(arr[i] - arr[i - 1]) ~= dir or math.abs(arr[i] - arr[i - 1]) > 3 or arr[i] == arr[i - 1] then
			is_valid = 0
		end
	end
	return is_valid
end

local function removeAt(arr, pos)
	local newArr = {}
	for i = 1, #arr do
		if i ~= pos then
			newArr[#newArr + 1] = arr[i]
		end
	end
	return newArr
end

-- Part 2 solution
local function solve_part2()
	local safe = 0
	for line in io.lines("in.txt") do
		local nums = split(line, " ")
		local line_safe = false
		for j = 1, #nums do
			local temp = removeAt(nums, j)
			if temp and is_safe(temp) == 1 then
				line_safe = true
				print(inspect(temp))
			end
		end
		safe = safe + (line_safe and 1 or 0)
	end
	return safe
end

local function real_solve() end

-- Solve and print results
print("Part 1:", solve_part1())
print("Part 2:", solve_part2())
real_solve()
