# elixir day2-2.exs

# x = horizontal, y = depth
r = File.read!("input.txt") |> String.split("\n") |> List.delete_at(-1)
|> Enum.reduce(%{:x => 0, :y => 0, :aim => 0}, fn line, acc ->
  [cmd, z] = String.split(line, " ")
  z = String.to_integer(z)
  case cmd do
    "forward" -> %{:x => acc[:x]+z, :y => acc[:y]+(z*acc[:aim]), :aim => acc[:aim]  }
    "up"      -> %{:x => acc[:x],   :y => acc[:y],               :aim => acc[:aim]-z}
    "down"    -> %{:x => acc[:x],   :y => acc[:y],               :aim => acc[:aim]+z}
  end
end)
IO.inspect(r)
IO.puts("depth*horizontal = #{r[:y] * r[:x]}")
