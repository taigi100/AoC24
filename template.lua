local function read_input(filename)
	local file = io.open(filename, "r")
	if not file then
		return nil
	end
	local content = file:read("*all")
	file:close()
	return content
end

local function dump(o, indent)
	indent = indent or ""
	if type(o) == "table" then
		local s = "{\n"
		for k, v in pairs(o) do
			if type(k) ~= "number" then
				k = '"' .. k .. '"'
			end
			s = s .. indent .. "  [" .. k .. "] = " .. dump(v, indent .. "  ") .. ",\n"
		end
		return s .. indent .. "}"
	else
		return tostring(o)
	end
end

-- Utility functions
local utils = {
	-- Split string by separator
	split = function(str, sep)
		if sep == nil then
			sep = "%s"
		end
		local t = {}
		for s in string.gmatch(str, "([^" .. sep .. "]+)") do
			table.insert(t, s)
		end
		return t
	end,

	-- Sum all numbers in a table
	sum = function(t)
		local s = 0
		for _, v in ipairs(t) do
			s = s + v
		end
		return s
	end,

	-- Convert string of digits to table of numbers
	digits_to_numbers = function(str)
		local t = {}
		for d in str:gmatch("%d") do
			table.insert(t, tonumber(d))
		end
		return t
	end,

	-- Get all numbers from a string
	get_numbers = function(str)
		local numbers = {}
		for num in str:gmatch("-?%d+") do
			table.insert(numbers, tonumber(num))
		end
		return numbers
	end,
}

-- Read input
local input = read_input("in.txt")
if not input then
	print("Error: Could not read input file")
	os.exit(1)
end

-- Parse input (modify as needed)
local lines = utils.split(input, "\n")

-- Part 1 solution
local function solve_part1(input_lines)
	-- Your solution here
	return "Not implemented"
end

-- Part 2 solution
local function solve_part2(input_lines)
	-- Your solution here
	return "Not implemented"
end

-- Solve and print results
print("Part 1:", solve_part1(lines))
print("Part 2:", solve_part2(lines))
