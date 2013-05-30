#!/usr/bin/env ruby
 
class Array
  def sample
    self[rand(count)]
  end
end
 
class Sq1Shape
  attr_reader :top, :bottom, :path_to
 
  def initialize(top = solved_top, bottom = solved_bottom, path_to = "")
    @top    = top
    @bottom = bottom
    @path_to = path_to
  end
 
  def turnable?
    top.first && bottom.first && top[6] && bottom[6]
  end
 
  def turn(amt_top, amt_bottom)
    amt_top    = (amt_top    + 12) % 12
    amt_bottom = (amt_bottom + 12) % 12
 
    new_top    = shift_by(top, amt_top)
    new_bottom = shift_by(bottom, amt_bottom)
 
    Sq1Shape.new(new_top, new_bottom, path_to + "(#{amt_top}, #{amt_bottom})")
  end
 
  def slash
    raise "can not turn" unless turnable?
    new_top    = bottom.take(6) + top.drop(6)
    new_bottom = top.take(6)    + bottom.drop(6)
 
    Sq1Shape.new(new_top, new_bottom, path_to + "/")
  end
 
  def neighbours
    possible_neighbours = (0..11).entries.product((0..11).entries)
    possible_neighbours.map! { |(t,b)| turn(t,b) }
    possible_neighbours = possible_neighbours.select(&:turnable?)
    possible_neighbours.map!(&:slash)
    possible_neighbours.uniq
  end
 
  def to_s
    path_to
  end
 
  # The maximal binary represetation of the top concattenated with the bottom
  def eql?(other)
    hash == other.hash
  end
 
  def hash
    max_bin_rep
  end
 
  private
 
  def max_bin_rep
    (max_bin_string(top) + max_bin_string(bottom)).to_i(2)
  end
 
  def max_bin_string(ary)
    shiftings(ary).map do |vals|
      vals.map { |val| val ? "1" : "0" }.join.to_i(2)
    end.max.to_s(2)
  end
 
  def shiftings(ary)
    (0...ary.count).map { |amt| shift_by(ary, amt) }
  end
 
  def shift_by(ary, amt)
    ary.drop(ary.count - amt) + ary.take(ary.count - amt)
  end
 
  def solved_top
    [true, false, true].cycle.take(12)
  end
 
  def solved_bottom
    [true, true, false].cycle.take(12)
  end
end
 
def away_by(n)
  states = [Sq1Shape.new]
  n.times do
    states = states.map(&:neighbours).flatten
    states.uniq!
  end 
  states
end
 
def run
  size = ARGV[0].to_i
  scrambles = away_by(size) - away_by(size-1)
  loop do
    puts scrambles.sample
    STDIN.gets
  end
end
 
run