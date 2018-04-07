library ieee;
    use ieee.std_logic_1164.all;

package my_pkg is
type foo_t is record
  a : std_logic_vector(7 downto 3);
  b : std_logic_vector(0 to 2);
end record;
type foo_vec_t is array(natural range <>) of foo_t;
end package my_pkg;

library ieee;
    use ieee.std_logic_1164.all;

    use work.my_pkg.all;

entity coco_test is
  port (
    -- System PORT
    clk        : in  std_logic;
    reset      : in  std_logic;

    stl_in     : in  std_logic_vector(8 downto 1);
    foo_in     : in  foo_t;

    foo_vec_in : in  foo_vec_t(0 to 2);

    stl_out    : out std_logic_vector(0 to 7)
  );
end coco_test;


architecture rtl of coco_test is

  constant const_foo  : foo_t := (5x"c", 3x"6");
  constant const_foov : foo_vec_t(foo_vec_in'range) := 
            ((5x"1d", 3x"6"), (5x"1e", 3x"3"), (5x"15", 3x"4"));

  signal sig_foo  : foo_t := const_foo;
  signal sig_foov : foo_vec_t(foo_vec_in'range) := const_foov;

begin

  test_proc : process(all)
  begin
    for i in stl_in'range loop
      stl_out(8-i) <= stl_in(i);
    end loop;
  end process;

end rtl;

