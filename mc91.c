int mc91(int n)
{
    if( n > 100 ) {
        return n - 10;
    } else {
        return mc91(mc91(n + 11));
    }
}
