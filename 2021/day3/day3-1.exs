# elixir day3-1.exs

r = File.read!("input.txt") |> String.split("\n") |> List.delete_at(-1)
|> Enum.reduce(%{:a=>0,:b=>0,:c=>0,:d=>0,:e=>0,:f=>0,:g=>0,:h=>0,:i=>0,:j=>0,:k=>0,:l=>0,:tot=>0}, fn line, acc ->
  [a,b,c,d,e,f,g,i,h,j,k,l] = String.split(line, "", trim: true) |> Enum.map(fn x -> String.to_integer(x) end)
  %{
    :a => acc[:a]+a,
    :b => acc[:b]+b,
    :c => acc[:c]+c,
    :d => acc[:d]+d,
    :e => acc[:e]+e,
    :f => acc[:f]+f,
    :g => acc[:g]+g,
    :h => acc[:h]+h,
    :i => acc[:i]+i,
    :j => acc[:j]+j,
    :k => acc[:k]+k,
    :l => acc[:l]+l,
    :tot => acc[:tot]+1,
  }
end)
IO.inspect(r)
# INCOMPLETE (FINISHED IN C)
